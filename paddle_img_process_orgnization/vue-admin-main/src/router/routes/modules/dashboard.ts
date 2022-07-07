import type { AppRouteModule } from '/@/router/types';

import { LAYOUT } from '/@/router/constant';
import { t } from '/@/hooks/web/useI18n';

const dashboard: AppRouteModule = {
  path: '/dashboard',
  name: 'Dashboard',
  component: LAYOUT,
  redirect: '/dashboard/analysis',
  meta: {
    orderNo: 10,
    icon: 'ion:grid-outline',
    title: "智能识别",
  },
  children: [
    
    {
      path: 'targetextraction',
      name: 'TargetExtraction',
      component: () => import('/@/views/dashboard/TargetExtraction.vue'),
      meta: {
        title: "目标提取",
      },
    },
    {
      path: 'changedetection',
      name: 'ChangeDetection',
      component: () => import('/@/views/dashboard/ChangeDetection.vue'),
      meta: {
        title: "变化检测",
      },
    },
    {
      path: 'targetdetection',
      name: 'TargetDetection',
      component: () => import('/@/views/dashboard/TargetDetection.vue'),
      meta: {
        title: "目标检测",
      },
    },
    {
      path: 'classificationoffeatures',
      name: 'ClassificationofFeatures',
      component: () => import('/@/views/dashboard/ClassificationofFeatures.vue'),
      meta: {
        title: "地物分类",
      },
    },
  ],
};

export default dashboard;
