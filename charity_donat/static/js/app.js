document.addEventListener("DOMContentLoaded", function () {
    /**
     * HomePage - Help section
     */

    class Help {
        constructor($el) {
            this.$el = $el;
            this.$buttonsContainer = $el.querySelector(".help--buttons");
            this.$slidesContainers = $el.querySelectorAll(".help--slides");
            this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
            this.init();
        }

        init() {
            this.events();
        }

        events() {
            /**
             * Slide buttons
             */
            this.$buttonsContainer.addEventListener("click", e => {
                if (e.target.classList.contains("btn")) {
                    this.changeSlide(e);
                }
            });

            /**
             * Pagination buttons
             */
            this.$el.addEventListener("click", e => {
                if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
                    this.changePage(e);
                }
            });
        }

        changeSlide(e) {
            e.preventDefault();
            const $btn = e.target;

            // Buttons Active class change
            [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
            $btn.classList.add("active");

            // Current slide
            this.currentSlide = $btn.parentElement.dataset.id;

            // Slides active class change
            this.$slidesContainers.forEach(el => {
                el.classList.remove("active");

                if (el.dataset.id === this.currentSlide) {
                    el.classList.add("active");
                }
            });
        }

        /**
         * TODO: callback to page change event
         */
        changePage(e) {
            e.preventDefault();
            const page = e.target.dataset.page;

            console.log(page);
        }
    }

    const helpSection = document.querySelector(".help");
    if (helpSection !== null) {
        new Help(helpSection);
    }

    /**
     * Form Select
     */
    class FormSelect {
        constructor($el) {
            this.$el = $el;
            this.options = [...$el.children];
            this.init();
        }

        init() {
            this.createElements();
            this.addEvents();
            this.$el.parentElement.removeChild(this.$el);
        }

        createElements() {
            // Input for value
            this.valueInput = document.createElement("input");
            this.valueInput.type = "text";
            this.valueInput.name = this.$el.name;

            // Dropdown container
            this.dropdown = document.createElement("div");
            this.dropdown.classList.add("dropdown");

            // List container
            this.ul = document.createElement("ul");

            // All list options
            this.options.forEach((el, i) => {
                const li = document.createElement("li");
                li.dataset.value = el.value;
                li.innerText = el.innerText;

                if (i === 0) {
                    // First clickable option
                    this.current = document.createElement("div");
                    this.current.innerText = el.innerText;
                    this.dropdown.appendChild(this.current);
                    this.valueInput.value = el.value;
                    li.classList.add("selected");
                }

                this.ul.appendChild(li);
            });

            this.dropdown.appendChild(this.ul);
            this.dropdown.appendChild(this.valueInput);
            this.$el.parentElement.appendChild(this.dropdown);
        }

        addEvents() {
            this.dropdown.addEventListener("click", e => {
                const target = e.target;
                this.dropdown.classList.toggle("selecting");

                // Save new value only when clicked on li
                if (target.tagName === "LI") {
                    this.valueInput.value = target.dataset.value;
                    this.current.innerText = target.innerText;
                }
            });
        }
    }

    document.querySelectorAll(".form-group--dropdown select").forEach(el => {
        new FormSelect(el);
    });

    /**
     * Hide elements when clicked on document
     */
    document.addEventListener("click", function (e) {
        const target = e.target;
        const tagName = target.tagName;

        if (target.classList.contains("dropdown")) return false;

        if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
            return false;
        }

        if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
            return false;
        }

        document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
            el.classList.remove("selecting");
        });
    });

    /**
     * Switching between form steps
     */
    class FormSteps {
        constructor(form) {
            this.$form = form;
            this.$next = form.querySelectorAll(".next-step");
            this.$prev = form.querySelectorAll(".prev-step");
            this.$step = form.querySelector(".form--steps-counter span");
            this.currentStep = 1;

            this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
            const $stepForms = form.querySelectorAll("form > div");
            this.slides = [...this.$stepInstructions, ...$stepForms];

            this.init();
        }

        /**
         * Init all methods
         */
        init() {
            this.events();
            this.updateForm();
        }

        /**
         * All events that are happening in form
         */
        events() {
            // Next step
            this.$next.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep++;
                    this.updateForm();
                });
            });

            // Previous step
            this.$prev.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep--;
                    this.updateForm();
                });
            });

            // Form submit
            this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
        }

        /**
         * Update form front-end
         * Show next or previous section etc.
         */
        updateForm() {
            this.$step.innerText = this.currentStep;
            if (this.currentStep === 3) {
                var checkboxes_button = document.querySelectorAll(".my-checkbox");
                checkboxes_button.forEach(function (checkbox) {
                    if (checkbox.checked) {
                        var id = checkbox.dataset.id;
                        $.get({
                            url: "/get_institutions/",
                            data: {checked_id: id}
                        }).done(function (response) {
                            $("#institution-list").html(response)

                        })
                    }
                })
            }


// TODO: Validation

            this.slides.forEach(slide => {
                slide.classList.remove("active");

                if (slide.dataset.step == this.currentStep) {
                    slide.classList.add("active");
                }
            });

            this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
            this.$step.parentElement.hidden = this.currentStep >= 6;

            if (this.currentStep === 5) {
                var $inputs = $("#form").find(".my-checkbox");
                var $summary = $("#form").find("div.summary span#podsumowanie_datki");
                var $amount = $("#form").find("div#amount input").val();
                var $institutions = $("#form").find("div#step3 input");
                var $picked_institution = $("#form").find("div.summary span#fundacja");
                var $bags = "worki";
                var $text_fundation = "Dla fundacji";
                var $personality_data = $("#form").find("div#personality_data input");
                var $street = $personality_data[0].value;
                var $city = $personality_data[1].value;
                var $postcode = $personality_data[2].value;
                var $phone = $personality_data[3].value;
                var $data = $personality_data[4].value;
                var $time = $personality_data[5].value;
                var $more_info = $("#form").find("div#uwaga textarea").val();
                var $adress_phone = $("#form").find("ul#adress_phone").children();
                var $data_hour_attension = $("#form").find("ul#data-hour-atension").children();

                var checkboxes = document.querySelectorAll(".my-checkbox");
                checkboxes.forEach(function (checkbox) {
                    if (checkbox.checked) {
                        var category_id = checkbox.id


                        $inputs.each(function () {
                            if (this.checked) {
                                var $new = $("<span>" + $amount + " " + $bags + " " + $(this).attr("name") + "</span>");
                                $summary.prepend($new)
                            }
                        });
                        var $institution_id = 0;
                        $institutions.each(function () {
                            if (this.checked) {
                                var $checked_institution = $("<span>" + $text_fundation + " " + $(this).attr("name") + "</span>");
                                $picked_institution.html($checked_institution);
                                $institution_id = this.id;

                            }
                        });
                        $adress_phone.eq(0).text($street);
                        $adress_phone.eq(1).text($city);
                        $adress_phone.eq(2).text($postcode);
                        $adress_phone.eq(3).text($phone);
                        $data_hour_attension.eq(0).text($data);
                        $data_hour_attension.eq(1).text($time);
                        $data_hour_attension.eq(2).text($more_info);

                        function getCookie(name) {
                            var cookieValue = null;
                            if (document.cookie && document.cookie !== '') {
                                var cookies = document.cookie.split(';');
                                for (var i = 0; i < cookies.length; i++) {
                                    var cookie = cookies[i].trim();
                                    // Does this cookie string begin with the name we want?
                                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                        break;
                                    }
                                }
                            }
                            return cookieValue;
                        }

                        var csrftoken = getCookie('csrftoken');
                        $("#potwierdzam").on("click", function () {

                            $.post({
                                url: "/add_donation/",
                                data: {
                                    csrfmiddlewaretoken: csrftoken,
                                    category_id: category_id,
                                    quantity: $amount,
                                    institution_id: $institution_id,
                                    adress: $street,
                                    city: $city,
                                    zip_code: $postcode,
                                    phone_number: $phone,
                                    pick_up_date: $data,
                                    pick_up_time: $time,
                                    pick_up_comment: $more_info
                                }, function() {
                                    console.log("poszło")
                                }
                            }).done(function () {
                                window.location.href = "http://127.0.0.1:8000/form_confirmation/#form-confirmation";
                            }).fail(function (e) {
                                alert("Nieposzło");
                                console.log(e)
                            });
                        });

                    }

                })
            }
        }

        /**
         * Submit form
         *
         * TODO: validation, send data to server
         */
        submit(e) {
            e.preventDefault();
            this.currentStep++;
            this.updateForm();
        }
    }

    const
        form = document.querySelector(".form--steps");

    if (form

        !==
        null
    ) {
        new

        FormSteps(form);
    }
})
;






