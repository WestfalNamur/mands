import type { NextPage } from "next";
import styles from "../styles/Home.module.css";

import LandingView from "../features/landingView";
import NavBar from "../features/layout/navBar";

const Home: NextPage = () => {
  return (
    <>
      <NavBar />
      <div className={styles.main}>
        <LandingView />
      </div>
    </>
  );
};

export default Home;
