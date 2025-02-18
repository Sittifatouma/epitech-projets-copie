<template>
  <div class="main-page">
    <div class="divs static static-one">
      <div class="header">
        <h1 class="first-titles">
          Virtual Reality for Mental Health Professionals VirtuHealth, an
          all-in-one VR
        </h1>
        <h3 class="third-title">platform trusted by over 15 therapists.</h3>
        <div class="wapper-button">
          <ButtonMain @click="showDemo">Démo</ButtonMain>
          <ButtonMain>Pricing</ButtonMain>
        </div>
      </div>
    </div>

    <div class="divp parallax parallax-one"></div>

    <div class="divs static static-two">
      <div class="digits">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <p>
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </div>
    </div>
    <div class="divp parallax parallax-two"></div>
    <div class="divs static static-three">
      aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
      voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
      sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
      mollit anim id est laborum.
    </div>
    <div class="divp parallax parallax-three"></div>
    <div class="divs static static-four">
      aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
      voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur
      sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
      mollit anim id est laborum.
    </div>
  </div>
</template>

<script>
import ButtonMain from "@/components/ButtonMain.vue";
export default {
  data() {
    return {};
  },
  methods: {
    showDemo() {
      window.open(
        "https://www.youtube.com/watch?v=ZH-esQfqycg&ab_channel=AmeliaVirtualCare"
      );
    },
  },
  components: {
    ButtonMain,
  },
};
</script>

<style scoped>
.main-page {
  height: 90vh;
  perspective: 3px;
  overflow-x: hidden;
}
.header {
  align-items: center;
}

.third-title {
  margin: 20px;
}
.wapper-button {
  display: flex;
  justify-content: center;
}
.divs {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 350px;
  font-size: 20px;
  text-transform: uppercase;
  transform-style: preserve-3d;
  font-weight: bold;
}
.divp {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 800px;
  font-size: 25px;
  text-transform: uppercase;
  transform-style: preserve-3d;
  font-weight: bold;
}

.static-one {
  background-color: #e7e9e8;
}

.static-two {
  background-color: #e7e9e8;
}

.static-three {
  background-color: #e7e9e8;
}
.static-four {
  background-color: #e7e9e8;
}

.parallax::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-repeat: no-repeat;
  background-size: 100vw auto;
  transform: translateZ(-0.9px) scale(1.7);
  z-index: -1;
}

.static {
  z-index: 1;
}
.parallax-one::after {
  background-image: url("../../public/img/background.jpg");
}

.parallax-two::after {
  background-image: url("../../public/img/doctor2.jpg");
}
.parallax-three::after {
  background-image: url("../../public/img/doctor1.jpg");
}
</style>
