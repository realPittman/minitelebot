import requests
import json
from .bot import Bot


class Methods(Bot):
    def __init__(self, Token, threadCount=100 ):
        super().__init__(Token, threadCount)
    
    def getMe(self):

        return self._sendRequest('getMe')
    
    def sendMessage(self,
                    chat_id, 
                    text, 
                    parse_mode=None,
                    disable_web_page_preview=None,
                    disable_notification=False,
                    reply_to_message_id=None,
                    reply_markup=None):

        data = {'chat_id': chat_id, 'text': text}

        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview

        return self._message('sendMessage', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def forwardMessage(self,
                       chat_id,
                       from_chat_id,
                       message_id,
                       disable_notification=None):

        data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}

        return self._message('forwardMessage', data, disable_notification=disable_notification)

    def sendPhoto(self,
                  chat_id,
                  photo,
                  caption=None,
                  parse_mode=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        data = {'chat_id': chat_id, 'photo': photo}

        if caption:
            data['caption'] = caption

        return self._message('sendPhoto', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def sendAudio(self,
                  chat_id,
                  audio,
                  caption=None,
                  parse_mode=None,
                  duration=None,
                  performer=None,
                  title=None,
                  thumb=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):
        data = {'chat_id': chat_id, 'audio': audio}
        if caption:
            data['caption'] = caption

        if duration:
            data['duration'] = duration

        if performer:
            data['performer'] = performer

        if title:
            data['title'] = title

        if thumb:
            data['thumb'] = thumb

        return self._message('sendAudio', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def sendDocument(self,
                     chat_id,
                     document,
                     caption=None,
                     thumb=None,
                     parse_mode=None,
                     disable_notification=None,
                     reply_to_message_id=None,
                     reply_markup=None
                     ):
        data = {'chat_id': chat_id, 'document': document}
        if caption:
            data['caption'] = caption

        if thumb:
            data['thumb'] = thumb

        return self._message('sendDocument', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def sendVideo(self,
                  chat_id,
                  video,
                  caption=None,
                  duration=None,
                  width=None,
                  height=None,
                  thumb=None,
                  parse_mode=None,
                  supports_streaming=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        data = {'chat_id': chat_id, 'video': video}

        if caption:
            data['caption'] = caption

        if duration:
            data['duration'] = duration

        if width:
            data['width'] = width

        if height:
            data['height'] = height

        if thumb:
            data['thumb'] = thumb

        if supports_streaming:
            data['supports_streaming'] = supports_streaming

        return self._message('sendVideo', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def sendAnimation(self,
                      chat_id,
                      animation,
                      caption=None,
                      duration=None,
                      width=None,
                      height=None,
                      thumb=None,
                      parse_mode=None,
                      disable_notification=None,
                      reply_to_message_id=None,
                      reply_markup=None):

        data = {'chat_id': chat_id, 'animation': animation}

        if caption:
            data['caption'] = caption

        if duration:
            data['duration'] = duration

        if width:
            data['width'] = width

        if height:
            data['height'] = height

        if thumb:
            data['thumb'] = thumb

        return self._message('sendAnimation', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def sendVoice(self,
                  chat_id,
                  voice,
                  caption=None,
                  parse_mode=None,
                  duration=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        data = {'chat_id': chat_id, 'voice': voice}

        if caption:
            data['caption'] = caption

        if duration:
            data['duration'] = duration

        return self._message('sendVoice', data, reply_to_message_id, disable_notification, reply_markup, parse_mode)

    def sendVideoNote(self,
                      chat_id,
                      video_note,
                      duration=None,
                      length=None,
                      thumb=None,
                      disable_notification=None,
                      reply_to_message_id=None,
                      reply_markup=None):

        data = {'chat_id': chat_id, 'video_note': video_note}

        if length:
            data['length'] = length

        if duration:
            data['duration'] = duration

        if thumb:
            data['thumb'] = thumb

        return self._message('sendVideoNote', data, reply_to_message_id, disable_notification, reply_markup)

    def sendMediaGroup(self,
                       chat_id,
                       media,
                       disable_notification=None,
                       reply_to_message_id=None):

        data = {'chat_id': chat_id, 'media': media}

        return self._message('sendMediaGroup', data, disable_notification=disable_notification, reply_to_message_id=reply_to_message_id)

    def sendLocation(self,
                     chat_id,
                     latitude,
                     longitude,
                     live_period=None,
                     disable_notification=None,
                     reply_to_message_id=None,
                     reply_markup=None):

        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude}

        if live_period:
            data['live_period'] = live_period

        return self._message('sendLocation', data, reply_to_message_id, disable_notification, reply_markup)

    def editMessageLiveLocation(self,
                                latitude,
                                longitude,
                                chat_id=None,
                                message_id=None,
                                inline_message_id=None,
                                reply_markup=None):

        data = {'latitude': latitude, 'longitude': longitude}

        if message_id:
            data['message_id'] = message_id,

        if chat_id:
            data['chat_id'] = chat_id

        if inline_message_id:
            data['inline_message_id'] = inline_message_id

        return self._message('editMessageLiveLocation', data, reply_markup=reply_markup)

    def stopMessageLiveLocation(self,
                                chat_id=None,
                                message_id=None,
                                inline_message_id=None,
                                reply_markup=None):

        data = {}

        if chat_id:
            data['chat_id'] = chat_id

        if message_id:
            data['message_id'] = message_id

        if inline_message_id:
            data['inline_message_id'] = inline_message_id

        return self._message('stopMessageLiveLocation', data, reply_markup=reply_markup)

    def sendVenue(self,
                  chat_id,
                  latitude,
                  longitude,
                  title,
                  address,
                  foursquare_id=None,
                  foursquare_type=None,
                  disable_notification=None,
                  reply_to_message_id=None,
                  reply_markup=None):

        data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'title': title, 'address': address}

        if foursquare_id:
            data['foursquare_id'] = foursquare_id

        if foursquare_type:
            data['foursquare_type'] = foursquare_type

        return self._message('sendVenue', data, reply_to_message_id, disable_notification, reply_markup)


    def sendContact(self,
                    chat_id,
                    phone_number,
                    first_name,
                    last_name=None,
                    vcard=None,
                    disable_notification=None,
                    reply_to_message_id=None,
                    reply_markup=None):

        data = {'chat_id': chat_id, 'phone_number': phone_number, 'first_name': first_name}

        if last_name:
            data['last_name'] = last_name

        if vcard:
            data['vcard'] = vcard

        return self._message('sendContact', data, reply_to_message_id, disable_notification, reply_markup)

    def sendChatAction(self,
                       chat_id,
                       action):

        data = {'chat_id': chat_id, 'action': action}

        return self._message('sendChatAction', data)

    def getUserProfilePhotos(self,
                             user_id,
                             offset=None,
                             limit=None):

        data = {'user_id': user_id}

        if offset:
            data['offset'] = offset

        if limit:
            data['limit'] = limit

        return self._message('getUserProfilePhotos', data)

    def answerCallbackQuery(self,
                            callback_query_id,
                            text,
                            show_alert=False,
                            url=None,
                            cache_time=0):

        data = {'callback_query_id': callback_query_id, 'text': text}

        if show_alert:
            data['show_alert'] = show_alert

        if url:
            data['url'] = url

        if cache_time:
            data['cache_time'] = cache_time

        return self._message('answerCallbackQuery', data)

    def editMessageText(self,
                        text,
                        chat_id=None,
                        message_id=None,
                        inline_message_id=None,
                        parse_mode=None,
                        disable_web_page_preview=None,
                        reply_markup=None):

        data = {'text': text}

        if chat_id:
            data['chat_id'] = chat_id

        if message_id:
            data['message_id'] = message_id

        if inline_message_id:
            data['inline_message_id'] = inline_message_id

        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview

        return self._message(method='editMessageText', data=data, parse_mode=parse_mode, reply_markup=reply_markup)

    def answerInlineQuery(self, inline_query_id, results, cache_time=0):

        data = {'inline_query_id': inline_query_id, 'results': json.dumps(results), 'cache_time': cache_time}

        return self._message('answerInlineQuery', data)

    def _message(self,
                 method,
                 data,
                 reply_to_message_id=None,
                 disable_notification=None,
                 reply_markup=None,
                 parse_mode=None):

        if disable_notification is not None:
            data['disable_notification'] = disable_notification

        if reply_to_message_id is not None:
            data['reply_to_message_id'] = reply_to_message_id

        if reply_markup is not None:
            data['reply_markup'] = reply_markup

        if parse_mode is not None:
            data['parse_mode'] = parse_mode
        return self._sendRequest(self._urlMethod(method), data)


