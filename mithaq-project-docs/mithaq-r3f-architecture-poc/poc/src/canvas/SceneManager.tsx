import { Scene01GavelSealProxy } from '../scenes/Scene01GavelSealProxy';
import { Scene02HeroProxy } from '../scenes/Scene02HeroProxy';
import { Scene03GapProxy } from '../scenes/Scene03GapProxy';
import { Scene04MethodProxy } from '../scenes/Scene04MethodProxy';
import { Scene05PillarsProxy } from '../scenes/Scene05PillarsProxy';
import { Scene06WorkshopsProxy } from '../scenes/Scene06WorkshopsProxy';
import { Scene07MentorsProxy } from '../scenes/Scene07MentorsProxy';
import { Scene08TrustProxy } from '../scenes/Scene08TrustProxy';
import { Scene09FAQProxy } from '../scenes/Scene09FAQProxy';
import { Scene10FinalCTAProxy } from '../scenes/Scene10FinalCTAProxy';
import { useMithaqStore } from '../store/mithaqStore';
import { Scene01MobileBenchmark } from '../audit/Scene01MobileBenchmark';

export function SceneManager() {
  const activeScene = useMithaqStore((state) => state.activeScene);
  const scene01Audit = typeof window !== 'undefined' && new URLSearchParams(window.location.search).get('audit') === 'mobile';

  switch (activeScene) {
    case 1:
      if (scene01Audit) {
        return <Scene01MobileBenchmark />;
      }
      return <Scene01GavelSealProxy />;
    case 2:
      return <Scene02HeroProxy />;
    case 3:
      return <Scene03GapProxy />;
    case 4:
      return <Scene04MethodProxy />;
    case 5:
      return <Scene05PillarsProxy />;
    case 6:
      return <Scene06WorkshopsProxy />;
    case 7:
      return <Scene07MentorsProxy />;
    case 8:
      return <Scene08TrustProxy />;
    case 9:
      return <Scene09FAQProxy />;
    case 10:
      return <Scene10FinalCTAProxy />;
    default:
      return <Scene01GavelSealProxy />;
  }
}
