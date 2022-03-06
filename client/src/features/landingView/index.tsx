import LandingViewTile from "./LandingViewTile";

import styles from "./LandingView.module.css"

// TODO
// xs:square causes problems when using via LandingView.module.css
const cssBlueTile = "h-16 bg-blue-500 xs:h-auto xs:square";
const cssPinkTile = "h-16 bg-pink-500 xs:h-auto xs:square";

export default function LandingView() {
  return (
    <div className={styles.div}>
      <h1 className={styles.h1}>
        <span className={styles.span}>Amanda</span>
      </h1>
      <p className={styles.p}>
        Everyone that knows Amanda can see that she is full of positive energy.
        One might wonder how such a big heart fits in such a small person?
      </p>
      <LandingViewTile
        imgSrc="/landingViewImages/dino.jpg"
        className={cssBlueTile}
      />
      <LandingViewTile
        imgSrc="/landingViewImages/mands_and_me.jpg"
        className={cssBlueTile}
      />
      <LandingViewTile
        imgSrc="/landingViewImages/manda.jpg"
        className={cssPinkTile}
      />
      <LandingViewTile
        imgSrc="/landingViewImages/family.jpg"
        className="h-16 bg-blue-500 xs:h-auto xs:square md:col-start-2"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/gisela.jpg"
        className={cssPinkTile}
      />
      <LandingViewTile
        imgSrc="/landingViewImages/mandela.jpg"
        className={cssBlueTile}
      />
      <LandingViewTile
        imgSrc="/landingViewImages/amanda_and_urquid.jpg"
        className={cssBlueTile}
      />
      <LandingViewTile
        imgSrc="/landingViewImages/caio_and_delagua.jpg"
        className={cssPinkTile}
      />
      <p className="self-center md:text-lg md:col-span-2 md:text-center md:px-4">
        But everything has a dark side... No chocolate is save from her!
        Nowhere!
      </p>
    </div>
  );
}
