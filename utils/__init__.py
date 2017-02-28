# # @login_required
# def dialogue_detail(request):
#     dialogue_id = request.GET.get('dialogue_id')
#     message_time = request.GET.get('message_time')
#     direction = request.GET.get('direction')
#
#     if not dialogue_id:
#         return CoastalJsonResponse(status=response.STATUS_400)
#
#     dialogue = Dialogue.objects.filter(id=dialogue_id).first()
#     if not dialogue:
#         return CoastalJsonResponse(status=response.STATUS_404)
#
#     messages = Message.objects.filter(dialogue=dialogue).order_by('-date_created')
#
#     if not (message_time or direction):
#         result = get_result(messages, request.user)
#
#     if (message_time or direction) and not (message_time and direction):
#         return CoastalJsonResponse(status=response.STATUS_400)
#
#     if message_time and direction:
#         message_time = datetime.datetime.strptime(message_time, '%Y-%m-%d %H:%M:%S')
#         message_time = timezone.make_aware(message_time, timezone.UTC())
#         if direction == 'up':
#             up_messages = messages.filter(date_created__lt=message_time)
#             result = get_result(up_messages, request.user)
#
#         if direction == 'down':
#             down_messages = messages.filter(date_created__gt=message_time)
#             result = get_result(down_messages, request.user)
#     result.update({'product_id': dialogue.product.id})
#     return CoastalJsonResponse(result)
#
#
# def get_result(query_message, user):
#     for single_message in query_message:
#         if single_message.receiver == user:
#             if not single_message.read:
#                 single_message.read = True
#                 single_message.save()
#
#     messages = messages[:20]
#     message_list = []
#     for message in messages:
#         message_dict = model_to_dict(message, fields=['id', 'sender', 'receiver', 'content'])
#         message_dict['date_created'] = message.date_created.strftime('%Y-%m-%d %H:%M:%S')
#         message_list.append(message_dict)
#     message_list.reverse()
#
#     result = {
#         'messages': message_list,
#     }
#     return result