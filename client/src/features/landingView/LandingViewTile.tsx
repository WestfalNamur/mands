import { useState } from "react";
import Image from "next/image";
import { useSpring, animated } from "react-spring";

interface Props {
  className: string;
  imgSrc: string;
}

export default function LandingViewTile(props: Props): JSX.Element {
  const { className, imgSrc } = props;
  const [hovered, setHovered] = useState(false);
  const styleProps = useSpring({ x: hovered ? 1 : 0 });

  return (
    <animated.div
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={className ? className : "h-16 xs:h-auto xs:square"}
      style={{
        transform: styleProps.x
          .to({
            output: [1, 1.1],
          })
          .to((x) => `scale(${x})`),
      }}
    >
      {hovered && (
        // https://stackoverflow.com/questions/67421778/next-js-image-layout-fill-is-broken
        <div style={{ width: "100%", height: "100%", position: "relative" }}>
          <Image src={imgSrc} alt="Dino" layout="fill" objectFit="cover" />
        </div>
      )}
    </animated.div>
  );
}
