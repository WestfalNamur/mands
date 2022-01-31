import { useState } from "react";
import { motion } from "framer-motion";
import Image from "next/image";

interface Props {
  className: string;
  imgSrc: string;
}

export default function LandingViewTile(props: Props): JSX.Element {
  const { className, imgSrc } = props;
  const [hovered, setHovered] = useState(false);

  return (
    <motion.div
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={className ? className : "h-16 xs:h-auto xs:square"}
      whileHover={{ scale: 1.1 }}
    >
      {hovered && (
        // https://stackoverflow.com/questions/67421778/next-js-image-layout-fill-is-broken
        <div style={{ width: "100%", height: "100%", position: "relative" }}>
          <Image src={imgSrc} alt="Dino" layout="fill" objectFit="cover" />
        </div>
      )}
    </motion.div>
  );
}
