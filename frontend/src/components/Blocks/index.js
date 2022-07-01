import userSVG from '@plone/volto/icons/user.svg';
import PersonBlockViewBlock from './PersonBlock/View';
import PersonBlockEditBlock from './PersonBlock/Edit';
import CampusBlockView from './CampusBlock/View';
import CampusBlockEdit from './CampusBlock/Edit';

const blocks = {
  personBlock: {
    id: 'personBlock',
    title: 'Person Block',
    icon: userSVG,
    group: 'uft',
    view: PersonBlockViewBlock,
    edit: PersonBlockEditBlock,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
  campusBlock: {
    id: 'campusBlock',
    title: 'Campus Block',
    icon: userSVG,
    group: 'uft',
    view: CampusBlockView,
    edit: CampusBlockEdit,
    restricted: false,
    mostUsed: true,
    sidebarTab: 1,
  },
};

export default blocks;
