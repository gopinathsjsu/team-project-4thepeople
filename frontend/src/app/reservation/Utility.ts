import * as moment from 'moment';
export class Utils {
    public static formatDate(date: any): string {
      if (date === undefined || date === null) {
        return '';
      } else {
        return moment(date).format('YYYY-MM-DD');
      }
    }
  }