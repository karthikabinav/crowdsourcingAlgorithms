fprintf('started');
%y1 = load('../meetup_dataset/user_group.mat');
%disp(y1);
%T1 = struct2table(y1);
%writetable(T1,'../meetup_dataset/user_group.csv', 'Delimiter', ',');
%fprintf('Done1');
%y2 = load('../meetup_dataset/user_event_ym.mat');
%T2 = struct2table(y2);
%writetable(T2,'../meetup_dataset/user_event_ym.csv', 'Delimiter', ',');
%fprintf('Done2');
%y3 = load('../meetup_dataset/event_group_time.mat');
%T3 = struct2table(y3);
%writetable(T3, '../meetup_dataset/event_group_time.csv', 'Delimiter', ',');
%fprintf('Done3');
%y1 = load('../meetup_dataset/event_location.mat');
%T1 = struct2table(y1);
%writetable(T1,'../meetup_dataset/event_location.csv', 'Delimiter', ',');
%fprintf('Done1');
%y2 = load('../meetup_dataset/group_tag.mat');
%T2 = struct2table(y2);
%writetable(T2,'../meetup_dataset/group_tag.csv', 'Delimiter', ',');
%fprintf('Done2');
%y3 = load('../meetup_dataset/meetup_user_tag.mat');
%T3 = struct2table(y3);
%writetable(T3,'../meetup_dataset/meetup_user_tag.csv', 'Delimiter', ',');
%fprintf('Done3');
y4 = load('../meetup_dataset/user_location.mat');
T4 = struct2table(y4);
writetable(T4,'../meetup_dataset/user_location.csv', 'Delimiter', ',');
fprintf('Done4');

