/**
 * Created by benoit on 04/07/2016.
 */

var patatesApp = angular.module('patatesApp', ['ui.bootstrap', 'ui.router', "ngAnimate"]);

patatesApp.config(function ($stateProvider, $urlRouterProvider) {

    //
    // For any unmatched url, redirect to /search
    $urlRouterProvider.otherwise("/home");
    //
    // Now set up the states
    $stateProvider
        .state('home', {
            url: "/home",
            templateUrl: "static/partials/home.html"
        })
        .state('about', {
            url: "/about",
            templateUrl: "static/partials/about.html"
        })
        .state('contact', {
            url: "/contact",
            templateUrl: "static/partials/contact.html"
        })
        .state('buy', {
            url: "/buy",
            templateUrl: "static/partials/buy.html"
        })
});