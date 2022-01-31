import type { NextPage } from "next";
import styles from "../styles/Home.module.css";

import LandingView from "../features/landingView";

const Home: NextPage = () => {
  return (
    <div className={styles.main}>
      <LandingView />
    </div>
  );
};

export default Home;
