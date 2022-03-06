import Link from "next/link";
import {useRouter} from "next/router";
import styles from "../Layout.module.css"

interface Props {
  href: string;
  text: string;
}

export default function NavBarLink(props: Props) {
  const {href, text} = props;
  const {asPath} = useRouter();

  const classNameLi = asPath == href ? "-mb-px mr-1" : "mr-1";
  const classNameA = asPath == href ? styles.aIsPath : styles.aIsNotPath;

  return (
    <li className={classNameLi}>
      <Link href={href}>
        <a className={classNameA} href="#">
          {text}
        </a>
      </Link>
    </li>
  );
}
