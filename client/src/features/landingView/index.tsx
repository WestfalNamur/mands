import LandingViewTile from "./LandingViewTile";

export default function LandingView() {
  return (
    <div className="p-4 max-w-5xl grid gap-4 xs:grid-cols-2 xs:p-8 md:grid-cols-4 lg:gap-6">
      <h1 className="text-4xl font-extrabold xs:col-span-2 xs:grid xs:gap-4 xs:grid-cols-2 md:col-span-3 md:text-5xl md:grid-cols-3 lg:text-6xl">
        <span className="md:col-span-2">Amanda</span>
      </h1>
      <p className="xs:row-start-2 xs:col-start-2 xs:self-center md:col-start-1 md:col-span-2 md:pr-12 md:text-lg">
        Everyone that knows Amanda can see that she is full of positive energy.
        One might wonder how such a big heart fits in such a small person?
      </p>
      <LandingViewTile
        imgSrc="/landingViewImages/dino.jpg"
        className="h-16 bg-blue-500 xs:h-auto xs:square"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/mands_and_me.jpg"
        className="h-16 bg-blue-500 xs:h-auto xs:square"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/manda.jpg"
        className="h-16 bg-pink-500 xs:h-auto xs:square"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/family.jpg"
        className="h-16 bg-blue-500 xs:h-auto xs:square md:col-start-2"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/gisela.jpg"
        className="h-16 bg-pink-500 xs:h-auto xs:square"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/mandela.jpg"
        className="h-16 bg-blue-500 xs:h-auto xs:square"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/amanda_and_urquid.jpg"
        className="h-16 bg-blue-500 xs:h-auto xs:square"
      />
      <LandingViewTile
        imgSrc="/landingViewImages/caio_and_delagua.jpg"
        className="h-16 bg-pink-500 xs:h-auto xs:square"
      />
      <p className="self-center md:text-lg md:col-span-2 md:text-center md:px-4">
        But everything has a dark side... No chocolate is save from her!
        Nowhere!
      </p>
    </div>
  );
}
