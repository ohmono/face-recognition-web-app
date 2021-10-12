import ApiService from "../common/api.service";
import { UPLOAD_IMAGE } from "./actions.type";

const actions = {
    [UPLOAD_IMAGE](context, image) {
        return ApiService.post("img", image).then(({ data }) => {
            return data
        })

    }
}

export default {
    actions
}