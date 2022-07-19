#! /usr/bin/python3

banner = r'''
###########################################################################
#                                                                         #

#                                  >> https://github.com/guiworldtv       #
###########################################################################

#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TNT SPORTS HD Op1 " tvg-logo="https://w7.pngwing.com/pngs/621/229/png-transparent-superliga-argentina-de-futbol-logo-tnt-sports-logo-sport-text-trademark-logo.png" group-title="DEPORTES",SPORTS: TNT SPORTS HD Op1 
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/94714
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:ESPN 1 DIRECTO ARG" tvg-logo="https://www.futbolenvivo.com.co/wp-content/uploads/2020/01/ESPN-2-en-vivo-online.jpg" group-title="DEPORTES",SPORTS:ESPN 1 DIRECTO ARG
https://delivery.cdn.rcs.net.ar/mnp/espn_hls/playlist.m3u8
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:ESPN 2 DIRECTO ARG" tvg-logo="https://www.futbolenvivo.com.co/wp-content/uploads/2020/01/ESPN-2-en-vivo-online.jpg" group-title="DEPORTES",SPORTS:ESPN 2 DIRECTO ARG
https://delivery.cdn.rcs.net.ar/mnp/espn2_hls/playlist.m3u8
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :Directv Sports 1 SD" tvg-logo="https://seeklogo.com/images/D/directv-sports-logo-6F86DBD521-seeklogo.com.png" group-title="DEPORTES",SPORTS: :Directv Sports 1 SD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53958
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Directv Sports 1 ARG FHD" tvg-logo="https://seeklogo.com/images/D/directv-sports-logo-6F86DBD521-seeklogo.com.png" group-title="DEPORTES",SPORTS: Directv Sports 1 ARG FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53959
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :Directv Sports 1" tvg-logo="https://seeklogo.com/images/D/directv-sports-logo-6F86DBD521-seeklogo.com.png" group-title="DEPORTES",SPORTS: :Directv Sports 1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/679
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :DirectvSP 2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/DirecTV_Sports_2_Latin_America_%282018%29.png/1200px-DirecTV_Sports_2_Latin_America_%282018%29.png" group-title="DEPORTES",SPORTS: :DirectvSP 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/680
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: :DirectvSP+ Plus" tvg-logo="https://www.pngfind.com/pngs/m/297-2974594_directv-sports-plus-logo-hd-png-download.png" group-title="DEPORTES",SPORTS: :DirectvSP+ Plus
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/678
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TYC SPORTS BUENOS AIRES" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/d/dc/TYC94.png" group-title="DEPORTES",SPORTS: TYC SPORTS BUENOS AIRES
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/66700
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: TyC Sports HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: TyC Sports HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58933
#EXTINF:-1 tvg-id="TYC SPORTS HD" tvg-name="SPORTS: TYC SPORTS PLAY(PARTIDOS)" tvg-logo="https://img2.freepng.es/20180723/huc/kisspng-logo-tyc-sports-brand-trademark-mosaic-5b55e9fa8e43a0.5446456715323571145827.jpg" group-title="DEPORTES",SPORTS: TYC SPORTS PLAY(PARTIDOS)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53792
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TYC Sports(directo solo arg)" tvg-logo="https://statics-files.tycsports.com/frontend/tycsports/img/site_image.jpg" group-title="DEPORTES",SPORTS: TYC Sports(directo solo arg)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/52688
#EXTINF:-1 tvg-id="TYC SPORTS HD" tvg-name="*SPORTS: HD:TYC SPORTS ARG FHD" tvg-logo="https://img2.freepng.es/20180723/huc/kisspng-logo-tyc-sports-brand-trademark-mosaic-5b55e9fa8e43a0.5446456715323571145827.jpg" group-title="DEPORTES",*SPORTS: HD:TYC SPORTS ARG FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/108
#EXTINF:-1 tvg-id="TYC SPORTS HD" tvg-name="*SPORTS: SD: TYC SPORTS ARG SD" tvg-logo="https://img2.freepng.es/20180723/huc/kisspng-logo-tyc-sports-brand-trademark-mosaic-5b55e9fa8e43a0.5446456715323571145827.jpg" group-title="DEPORTES",*SPORTS: SD: TYC SPORTS ARG SD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/34478
#EXTINF:-1 tvg-id="Canal TyC Sports" tvg-name="SPORTS: TYC Sport USA" tvg-logo="" group-title="DEPORTES",SPORTS: TYC Sport USA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/20252
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: FOX SPORTS 1 ARG FHD" tvg-logo="https://play.foxsportsla.com/assets/images/Logo-FS.png" group-title="DEPORTES",SPORTS: FOX SPORTS 1 ARG FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/3668
#EXTINF:-1 tvg-id="FOX Sports" tvg-name="SPORTS SUR: Fox Sports 1 ARG HD" tvg-logo="http://zpapi.zetatv.com.uy/media/images/fox-sports.png" group-title="DEPORTES",SPORTS SUR: Fox Sports 1 ARG HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/41745
#EXTINF:-1 tvg-id="FOX Sports 2" tvg-name="SPORTS SUR: Fox Sports 2 ARG" tvg-logo="http://zpapi.zetatv.com.uy/media/images/fox-sports-2.png" group-title="DEPORTES",SPORTS SUR: Fox Sports 2 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/41746
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:  ESPN EX  FOX SPORTS PREMIUM Op1" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fox_Sports_Premium_Argentina_2020.png" group-title="DEPORTES",SPORTS:  ESPN EX  FOX SPORTS PREMIUM Op1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16521
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: ESPN  EX Fox Sports Premium Op2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fox_Sports_Premium_Argentina_2020.png" group-title="DEPORTES",SPORTS: ESPN  EX Fox Sports Premium Op2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/693
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN EX  FOX SPORTS PREMIUM Op3 " tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/cf/Fox_Sports_Premium_Argentina_2020.png" group-title="ARGENTINA 1",SPORTS: ESPN EX  FOX SPORTS PREMIUM Op3 
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16229
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: HD:TNT SPORTS Op2" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/46/TNT_Sports_Logo_Vertical_%282017%29.png" group-title="DEPORTES",SPORTS: HD:TNT SPORTS Op2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/99
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: HD:TNT SPORTS Op3" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/46/TNT_Sports_Logo_Vertical_%282017%29.png" group-title="DEPORTES",SPORTS: HD:TNT SPORTS Op3
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17095
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: HD:TNT SPORTS Op4" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/46/TNT_Sports_Logo_Vertical_%282017%29.png" group-title="DEPORTES",SPORTS: HD:TNT SPORTS Op4
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17096
#EXTINF:-1 tvg-id="ESPN" tvg-name="SPORTS: ESPN 1 SUR AR" tvg-logo="https://a1.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fespn_logos%2Fespn_red.png" group-title="DEPORTES",SPORTS: ESPN 1 SUR AR
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/41620
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 2 ARG" tvg-logo="http://elmasteriptv.com:8000/images/017f41a2ef4ff9d39f45f680b88cd23b.jpg" group-title="DEPORTES",SPORTS: ESPN 2 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16663
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: ESPN 1 ARG" tvg-logo="https://cdn.mitvstatic.com/channels/pe_espn_m.png" group-title="DEPORTES",SPORTS: ESPN 1 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16662
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 2 ARG 2" tvg-logo="http://elmasteriptv.com:8000/images/017f41a2ef4ff9d39f45f680b88cd23b.jpg" group-title="DEPORTES",SPORTS: ESPN 2 ARG 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31740
#EXTINF:-1 tvg-id="ESPN 2" tvg-name="SPORTS: ESPN 2 LINE ARG" tvg-logo="https://www.futbolenvivo.com.co/wp-content/uploads/2020/01/ESPN-2-en-vivo-online.jpg" group-title="DEPORTES",SPORTS: ESPN 2 LINE ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/32157
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 3 ARG" tvg-logo="http://elmasteriptv.com:8000/images/021ee6585dd4256f549242057e972f41.png" group-title="DEPORTES",SPORTS: ESPN 3 ARG
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16664
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: ESPN 2 FHD" tvg-logo="http://www.cooprico.com.ar/images/historic/canales/espn2.png" group-title="DEPORTES",SPORTS: ESPN 2 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31237
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Espn HD M" tvg-logo="http://elmasteriptv.com:8000/images/42fa21e42f99f88f0a881e12119ae313.jpg" group-title="DEPORTES",SPORTS: Espn HD M
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17493
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: ESPN + PLUS HD" tvg-logo="https://springboard-cdn.appadvice.com/wp-content/appadvice-v2-media/2018/02/espn-plus_dbc67d58aaa156a0ed06d06dd4972971-xl.jpg" group-title="DEPORTES",SPORTS: ESPN + PLUS HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/12157
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: WIN SPORTS + PLUS COLOMBIA" tvg-logo="https://futbolete.com/wp-content/uploads/2019/12/capturadepantall-f0f54bcde7fc1471047f7b0e52fe8147-1200x600-1.jpg" group-title="DEPORTES",SPORTS: WIN SPORTS + PLUS COLOMBIA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/16492
#EXTINF:-1 tvg-id="" tvg-name="Sports:Win Sport + 2" tvg-logo="https://futbolete.com/wp-content/uploads/2019/12/capturadepantall-f0f54bcde7fc1471047f7b0e52fe8147-1200x600-1.jpg" group-title="DEPORTES",Sports:Win Sport + 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/43501
#EXTINF:-1 tvg-id="Canal ESPN+ Latinoamérica" tvg-name="SPORTS: HD:ESPN +" tvg-logo="https://secure.espncdn.com/watchespn/images/espnplus/paywalls/ESPN_PLUS.logo@2x.png" group-title="DEPORTES",SPORTS: HD:ESPN +
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4296
#EXTINF:-1 tvg-id="Canal ESPN Deportes" tvg-name="SPORTS: ESPN DEPORTES HD" tvg-logo="https://a1.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fespn_logos%2Fespndeportes_white.png" group-title="DEPORTES",SPORTS: ESPN DEPORTES HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/15490
#EXTINF:-1 tvg-id="Canal Fox Deportes" tvg-name="SPORTS: FOX DEPORTES HD" tvg-logo="https://is2-ssl.mzstatic.com/image/thumb/Purple123/v4/c3/f9/36/c3f936b0-4109-35e5-c22e-0ac53d9213f6/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-10.png/1200x630wa.png" group-title="DEPORTES",SPORTS: FOX DEPORTES HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/15488
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="SPORTS: Fox Sports 1 LA" tvg-logo="https://play.foxsportsla.com/assets/images/Logo-FS.png" group-title="DEPORTES",SPORTS: Fox Sports 1 LA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/12311
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: FOX SPORTS 1 SUR" tvg-logo="https://play.foxsportsla.com/assets/images/Logo-FS.png" group-title="DEPORTES",SPORTS: FOX SPORTS 1 SUR
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/12312
#EXTINF:-1 tvg-id="FOX Sports 3" tvg-name="*SPORTS: HD:FOX SPORTS 3" tvg-logo="https://static.wixstatic.com/media/0cd32b_36fc7a2ba14b4a81937ee99c0c5dd9f8.png" group-title="DEPORTES",*SPORTS: HD:FOX SPORTS 3
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/101
#EXTINF:-1 tvg-id="" tvg-name="Sports:DIRECTV SPORTS 1 ECUADOR" tvg-logo="" group-title="DEPORTES",Sports:DIRECTV SPORTS 1 ECUADOR
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/326
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: TNT SPORT 1 CHILE" tvg-logo="http://1.bp.blogspot.com/-H0bRRXbMOwo/UhEC37cIzGI/AAAAAAAAOnU/plUJ7hWqclI/s1600/cdf+NUEVO.png" group-title="DEPORTES",SPORTS: TNT SPORT 1 CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31268
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL TNT SPORT 3 CHILE" tvg-logo="https://i.imgur.com/lEc55se.png" group-title="DEPORTES",SPORTS_CL TNT SPORT 3 CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31270
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL:  ESTADIO TNT SPORT CHILE" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/f/fa/Logocdfpremium2019.png/revision/latest?cb=20190216005645" group-title="DEPORTES",SPORTS_CL:  ESTADIO TNT SPORT CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31271
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL TNT SPORT Premium CHILE" tvg-logo="https://i.imgur.com/lEc55se.png" group-title="DEPORTES",SPORTS_CL TNT SPORT Premium CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31272
#EXTINF:-1 tvg-id="" tvg-name="SPORTS_CL TNT SPORT 1 CHILE" tvg-logo="https://cdn.mitvstatic.com/programs/cl_cdf-premium_p_m.jpg" group-title="DEPORTES",SPORTS_CL TNT SPORT 1 CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31275
#EXTINF:-1 tvg-id="TNT SPORTS" tvg-name="*SPORTS: HD:GOLF CHANNEL" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTfDr5DY-PFDZnDKbK-nrOZ4eyYfLyfvfIUcWfFNNpqn0LwCLTw" group-title="DEPORTES",*SPORTS: HD:GOLF CHANNEL
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/107
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Bolivia Deportes" tvg-logo="http://directostv.teleame.com/wp-content/uploads/2018/02/bolivia-deportes.png" group-title="DEPORTES",SPORTS: Bolivia Deportes
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/387
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: CDO BASICO CHILE" tvg-logo="http://directostv.teleame.com/wp-content/uploads/2018/06/cdo.png" group-title="DEPORTES",SPORTS: CDO BASICO CHILE
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/377
#EXTINF:-1 tvg-id="Canal Movistar Fórmula 1" tvg-name="SPORTS: F1 FHD" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/7/70/DAZN_F1_logo.png" group-title="DEPORTES",SPORTS: F1 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/211
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: FUTV HD" tvg-logo="" group-title="DEPORTES",SPORTS: FUTV HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/19136
#EXTINF:-1 tvg-id="El Garage" tvg-name="SPORTS: GARAGE TV" tvg-logo="https://static.wixstatic.com/media/a6f875_c7ca84d7360f45ffb13d840b0649654e.png" group-title="DEPORTES",SPORTS: GARAGE TV
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/385
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: MLB Live" tvg-logo="https://static1.squarespace.com/static/5bdfef0a697a98c05dd88ac0/5be3acea8985830adc1dc1f8/5c4fa2cc7ba7fc601bbd68c1/1548723770231/mlb.jpg?format=300w" group-title="DEPORTES",SPORTS: MLB Live
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/380
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: MLB Network" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8OvbTbRC3ih2o9AabgcJUPH6mXoGT232CfiMu78FDWmpIana8" group-title="DEPORTES",SPORTS: MLB Network
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/379
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Real Madrid TV" tvg-logo="https://media.cdnandroid.com/19/0b/92/cc/imagen-real-madrid-tv-0thumb.jpg" group-title="DEPORTES",SPORTS: Real Madrid TV
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/382
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: Red Bull TV" tvg-logo="https://image.redbull.com/rbcom/010/2016-10-01/1331821221085_2/0010/1/1050/656/1/red-bull-tv.png" group-title="DEPORTES",SPORTS: Red Bull TV
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/381
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: UFC NETWORK" tvg-logo="https://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500/ufc.png" group-title="DEPORTES",SPORTS: UFC NETWORK
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/378
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO PARAGUAY1" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO PARAGUAY1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4230
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO PARAGUAY2" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO PARAGUAY2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4229
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO SPORT CR 1" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO SPORT CR 1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4235
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO SPORTS 1 HD (BOLIVIA)" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO SPORTS 1 HD (BOLIVIA)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4234
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:TIGO SPORTS 2 HD (BOLIVIA)" tvg-logo="" group-title="DEPORTES",SPORTS:TIGO SPORTS 2 HD (BOLIVIA)
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/4232
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:BE-IN,  LALIGA 1HD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS:BE-IN,  LALIGA 1HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31347
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:BE IN,  SPORTS LA LIGA HD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS:BE IN,  SPORTS LA LIGA HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31348
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 11 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 11 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31349
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 10 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 10 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31350
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 9 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 9 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31351
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 8 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 8 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31352
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 7 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 7 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31353
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 5 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 5 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31354
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 2 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 2 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31355
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 1 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 1 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31356
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 3 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 3 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31357
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 4 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 4 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31358
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 6 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 6 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31359
#EXTINF:-1 tvg-id="" tvg-name="SPORTS arb: BE IN,  SPORTS 12 FHD" tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS arb: BE IN,  SPORTS 12 FHD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31360
#EXTINF:-1 tvg-id="" tvg-name="SPORTS us: BE IN,  SPORTS Ñ la liga " tvg-logo="http://1.bp.blogspot.com/-4Wx5_LP1YJM/UjzhGIrKNlI/AAAAAAAACbI/4HmsX_hGkyg/s1600/imagSPORTS.jpg" group-title="DEPORTES 2",SPORTS us: BE IN,  SPORTS Ñ la liga 
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31362
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:SK Y SPORTS 21" tvg-logo="https://www.thSPORTSun.co.uk/wp-content/uploads/2018/09/NINTCHDBPICT000353771160.jpg" group-title="DEPORTES 2",SPORTS:SK Y SPORTS 21
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31365
#EXTINF:-1 tvg-id="" tvg-name="SPORTS:SK Y SPORTS 16" tvg-logo="https://www.thSPORTSun.co.uk/wp-content/uploads/2018/09/NINTCHDBPICT000353771160.jpg" group-title="DEPORTES 2",SPORTS:SK Y SPORTS 16
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/31366
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: AYM Sports MEX" tvg-logo="http://elmasteriptv.com:8000/images/3f76d5d70b7fb3340973142ca42cc9f3.png" group-title="DEPORTES",SPORTS: AYM Sports MEX
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/17453
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: DAZN" tvg-logo="https://queadslcontratar.com/sites/default/files/images/logos/dazn-200x300.png" group-title="DEPORTES",SPORTS: DAZN
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/40725
#EXTINF:-1 tvg-id="" tvg-name="ECU:El canal del Futbol" tvg-logo="https://www.xtrim.tv/images/xtr-vod-item-logo-ecdf.png" group-title="DEPORTES",ECU:El canal del Futbol
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/53975
#EXTINF:-1 tvg-id="" tvg-name="SPORTS: WIN SPORTS HD + PLUS COLOMBIA" tvg-logo="https://futbolete.com/wp-content/uploads/2019/12/capturadepantall-f0f54bcde7fc1471047f7b0e52fe8147-1200x600-1.jpg" group-title="DEPORTES",SPORTS: WIN SPORTS HD + PLUS COLOMBIA
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58631
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: TNT Sports" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: TNT Sports
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58930
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: DIRECTV Sports Plus" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: DIRECTV Sports Plus
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58931
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: DIRECTV Sports 2" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: DIRECTV Sports 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58932
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN Argentina HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN Argentina HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58934
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN 3 Sur HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN 3 Sur HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58935
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN 2 Sur HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN 2 Sur HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58936
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: ESPN Extra" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: ESPN Extra
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58937
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports Premium" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports Premium
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58938
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports Sur" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports Sur
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58939
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports Sur 2" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports Sur 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58940
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Fox Sports 3 Sur" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Fox Sports 3 Sur
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58941
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: IVC Net HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: IVC Net HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58942
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: DeporTV HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: DeporTV HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58943
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: NBA TV International HD" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: NBA TV International HD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58944
#EXTINF:-1 tvg-id="" tvg-name="SPORTS-ARG: Golf Channel" tvg-logo="" group-title="DEPORTES 2",SPORTS-ARG: Golf Channel
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/58945
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 1" tvg-logo="https://i.ibb.co/61yhwrb/2560px-Ty-C-Sports-play-1-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 1
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70616
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 2" tvg-logo="https://i.ibb.co/z2mbPB5/2560px-Ty-C-Sports-play-2-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 2
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70617
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 3" tvg-logo="https://i.ibb.co/7XmctpY/2560px-Ty-C-Sports-play-3-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 3
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70618
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 4" tvg-logo="https://i.ibb.co/WWnWQ0V/2560px-Ty-C-Sports4-logo-svg.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 4
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70619
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 5" tvg-logo="https://i.ibb.co/yP7hzk1/2560px-Ty-C-Sports5-logo-svg-1.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 5
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70620
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 6" tvg-logo="https://i.ibb.co/jrdckjY/2560px-Ty-C-Sports6-logo-svg-2.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 6
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70621
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 7" tvg-logo="https://i.ibb.co/f18yLZs/2560px-Ty-C-Sports7-logo-svg-3.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 7
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70622
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 8" tvg-logo="https://i.ibb.co/Tv0xLW4/2560px-Ty-C-Sports8-logo-svg-4.png" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 8
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70623
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 9" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlT9TyPbVEmRmTrv3cg-Ta5g_DDjs2N-F6Eg&usqp=CAU" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 9
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70624
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TyC SPORT PLAY 10" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTlT9TyPbVEmRmTrv3cg-Ta5g_DDjs2N-F6Eg&usqp=CAU" group-title="EVENTOS",EVENTOS: TyC SPORT PLAY 10
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70625
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TNT Sports Brasil" tvg-logo="https://upload.wikimedia.org/wikipedia/pt/d/dc/Logotipo_TNT_Sports.png" group-title="EVENTOS",EVENTOS: TNT Sports Brasil
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70626
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TNT Sports 2 Brasil" tvg-logo="https://upload.wikimedia.org/wikipedia/pt/d/dc/Logotipo_TNT_Sports.png" group-title="EVENTOS",EVENTOS: TNT Sports 2 Brasil
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70627
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: TNT Sports 4 Brasil" tvg-logo="https://upload.wikimedia.org/wikipedia/pt/d/dc/Logotipo_TNT_Sports.png" group-title="EVENTOS",EVENTOS: TNT Sports 4 Brasil
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70628
#EXTINF:-1 tvg-id="" tvg-name="EVENTOS: F1FULLHFD" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/7/70/DAZN_F1_logo.png" group-title="EVENTOS",EVENTOS: F1FULLHFD
http://elmasteriptv.com:8000/Ivanmart/PEtBhjMDDkKJ/70795


#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.portalpopcyber.com/wp-content/uploads/2021/10/mtv-logo-952x630.png",MTV LATINOAMERICA
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/MTV_HD/SA_SAGEMCOM/MTV_HD.m3u8
#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD.m3u8
#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 2
http://181.30.129.66:80/live/live2/ArtearHD/SA_Live_fta/ArtearHD.m3u8

#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 3
https://live-01-02-eltrece.vodgc.net/eltrecetv/tracks-v1a1/mono.m3u8


#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 4
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/ArtearHD.m3u8

#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png",El Trece 5
http://jumangis.com:2082/Sv503iptv22/QR7E5sm3J2/95534



#EXTINF:-1  tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png", EL TRECE INTERNACIONAL
http://jumangis.com:2082/Sv503iptv22/QR7E5sm3J2/95506

#EXTINF:-1 tvg-logo="https://i.imgur.com/srtddlN.png" group-title="Argentina",TV Publica
https://delivery.cdn.rcs.net.ar/mnp/tvp/output.mpd

#EXTINF:-1 tvg-logo="https://i.imgur.com/IS4LViL.png" group-title="Argentina",El Nueve
https://delivery.cdn.rcs.net.ar/mnp/elnueve/output.mpd








#EXTINF:-1 group-title="Argentina" tvg-logo="https://yt3.ggpht.com/ytc/AKedOLSYU51c8SbrkWZeNBRMFeCnGv0YXPpXuEGBNq-X5g=s88-c-k-c0x00ffffff-no-rj",Encuentro
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Encuentro.m3u8


#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",Telefe
http://titanlivetv.com:8080/8cEW8XH37tDT/GP4qLxWhcCkd/111675

#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",Telefe
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8



#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 2
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/TelefeHD.m3u8
#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 3
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/TelefeHD-edge9.m3u8
#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 4
http://jumangis.com:2082/Sv503iptv22/QR7E5sm3J2/95508
#EXTINF:-1 tvg-id="Telefe" tvg-name="Telefe" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE 5
https://delivery.cdn.rcs.net.ar/mnp/telefe/output.mpd

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",América TV
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/AmericaTV/SA_SAGEMCOM/AmericaTV.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",IP - Información Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8

#EXTINF:-1 group-title="Argentina",el siete (tv publica)
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal7.m3u8

#EXTINF:-1 group-title="Argentina",EL NUEVE HD
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal9.m3u8

#EXTINF:-1 group-title="Argentina",encuentro
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/playlist.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg/260px-Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg.png" group-title="NOTICIAS", IP  24.5         
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=4499968.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="http://www.grupocronica.com.ar/mediakit/wp-content/uploads/2017/10/cronica-hd-con-sombra-grande.png" , CRONICA HD  24.4
https://g5.vxral-slo.transport.edge-access.net/b10/ngrp:cronicatv_video1-100044_all/cronicatv_video1-100044_720p/index.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/LogoCanal26.png/120px-LogoCanal26.png" , CANAL 26  24.2
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w794690609_b2628000_sleng.m3u8

#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/A24_%282019-1%29.png/150px-A24_%282019-1%29.png" , A24  36.3
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056_720p.m3u8



#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/c8/Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png" group-title="Argentina", AMERICA HD  36.1
https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/b/b0/Canal9.jpg" group-title="Argentina", CANAL 9  35.1 
https://ar-elnueve-elnueve-live.ned.media/live.m3u8?iut=eyJwYXJhbXMiOnsiZXhwIjoxNjI5NDY0OTI5LCJzZXNzaW9uIjoiMTgxLjQ0LjEyOS43MSIsIndoaXRlbGlzdCI6WyIxODEuNDQuMTI5LjcxIl19LCJzaWduYXR1cmUiOiJjNzQ2NTZjMjM0MjI5MmYwMDBhMzExZjNlYWIzMzBlNzVmYjJmNzY1In0=



#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5f523aa5523ae000074745ec/colorLogoPNG.png" group-title="NOTICIAS", TELEFÉ NOTICIAS
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5f523aa5523ae000074745ec/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff334c2-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=dffc36b9-57c6-4973-9903-2f83d465ac40&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/8f/Canal13_logo.png" group-title="Argentina", CANAL 13  33.1
http://edge5-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD-avc1_379968=10016.m3u8



#EXTINF:-1 tvg-logo="https://scontent.fepa11-1.fna.fbcdn.net/v/t1.6435-9/206638151_10223169123710059_3666810289391430657_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=825194&_nc_eui2=AeGxugJ54qa7RhgKBnLTrHOu14OonvQq8lrXg6ie9CryWkCQzaYyrufVmZGkiprZVM0&_nc_ohc=dbLCQPiMFxEAX9X0jrT&_nc_ht=scontent.fepa11-1.fna&oh=afeef92e5377cb7720df7b2f4afc60c8&oe=6127F95F" group-title="Argentina", SSIPTV ARG TV
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5df265697ec3510009df1ef0/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1d530-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=ec2383fd-6e28-4df5-9d1c-b66eee700e0c&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Net_TV_logo.png/120px-Net_TV_logo.png" group-title="Argentina", NET TV  27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Paka-paka.svg/245px-Paka-paka.svg.png" group-title="Argentina", PAKA PAKA  22.2
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_The_Simpsons.svg/1200px-Logo_The_Simpsons.svg.png" group-title="Argentina", LOS SIMPSONS
https://videostreaming.cloudserverlatam.com/cloudservertv/cloudservertv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/Logomagic96.png" group-title="Argentina", MAGIC KIDS
https://live.admefy.com/live/clean_peach_ef224.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Cine.Ar_logo.svg/1280px-Cine.Ar_logo.svg.png" group-title="Argentina", CINEAR  22.4
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8   

#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5de91cf02fc07c0009910465/colorLogoPNG.png" group-title="Argentina", TELEFÉ CLÁSICO
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5de91cf02fc07c0009910465/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1ae23-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=a367d0d9-b23d-4bb5-8d48-55f0cbeac4fb&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/gwVNQhVICXN4Q7djaLyeQGCiMAa4Jum_PqeVaFZ1W90T4Y0G297wC1upnHRcKUbA6Q=w412-h220-rw" group-title="Argentina", GEN TV  17.3
https://videohd.live:19360/8010/8010.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Od4eldPqILM/XjtCKHxeYSI/AAAAAAAAvok/HDnuaXs9cCsFzbr0QrQtw3bYeDB0_5osACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CINCO TV TIGRE  30.1
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://neotvdigital.com.ar/imagenes/logo1.png" group-title="Argentina", NEO TV DIGITAL  14.1
https://videostream.shockmedia.com.ar:19360/neotvdigital/neotvdigital.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMm0MM0BtkhB9xHWsECtnky05aGfA8KKnDSg&usqp=CAU" group-title="Argentina", CANAL 29 QUILMES 18.1
http://inliveserver.com:1935/8386/8386/playlist.m3u8

#EXTINF:-1 tvg-logo="https://serenotv.com/wp-content/uploads/2020/08/canal-telecreativa.jpg" group-title="Argentina", TELECREATIVA LANUS
https://panel.dattalive.com/8012/8012/playlist.m3u8

#EXTINF:-1 tvg-logo="https://image.winudf.com/v2/image1/Y29tLmExMjNmcmVlYXBwcy5mcmVlLmFwcDVkNWVjMWY4ODliOThfaWNvbl8xNTY3NjE5OTcxXzAxNw/icon.png?w=170&fakeurl=1" group-title="Argentina", CANAL 4 TELEAIRE SAN MARTIN
https://stmvideo2.livecastv.com/canal4/canal4/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-SlqJrd0GiYk/XjtCBz2FbhI/AAAAAAAAvog/HkkKzNWrEOYiE08Rdlw-mxsDtzpJ_zD8wCK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CANAL 6 MORENO
https://5975e06a1f292.streamlock.net:4443/canal6moreno/canal6moreno/playlist.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VIC2PROV.png" group-title="Argentina", PROVINCIAL TV
http://www.trimi.com.ar/provincial/streaming/mystreamProvincialHSMed.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG3riJIJamJMTaIwOIMuqH2cdOfdLQIyz9-NHeJ-pF2tQJsM-akUEu5MuYVspASJxZNQ&usqp=CAU" group-title="Argentina", CIUDAD MAGAZINE
https://g4.mc-slo.transport.edge-access.net/a09/ngrp:magazine_live01-100083_all/magazine_live01-100083_720p.m3u8

#EXTINF:-1 tvg-logo="http://www.canalkzo.com/images/lg_kzo.svg" group-title="Argentina", KZO
http://g2.vxral-slo.transport.edge-access.net/nx-beta/nx.hor.livetx.01/5eaa642772b3a25e2c28699e_540p/index.m3u8



#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/TYC_SPORTS.jpg/800px-TYC_SPORTS.jpg" group-title="Argentina", TyC SPORT 
https://d3055hobuue3je.cloudfront.net/out/v1/b841c366cbe540e6a106c3ba83e5c8d6/index.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/NTNvh66/header-ciudadmagica.jpg" group-title="DEPORTE", CIUDAD MAGICA TV
https://srv2.zcast.com.br/ciudadm/ciudadm/playlist.m3u8


#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-2gN4wEv_qPI/XjtKDwMuIQI/AAAAAAAAvrY/VTtJwZALBykDRnM8ia0Xbqi0FbREvdrZACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", GARAGE TV
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist_w2049053275_b1296000_sleng.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/150px-Deutsche_Welle_symbol_2012.svg.png" group-title="NOTICIAS", DW ESPAÑOL
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/stream05/streamPlaylist.m3u8

#EXTINF:-1 tvg-logo="http://tvabierta.weebly.com/uploads/5/1/3/4/51344345/mirador.png" group-title="Argentina", MIRADOR  22.3
https://5fb24b460df87.streamlock.net/live-cont.ar/mirador/playlist.m3u8 

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/4c/Telemax.png" group-title="Argentina", TELEMAX  26.3
https://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://d2ucqd3jt48qxz.cloudfront.net/img/footer-logo.png" group-title="Argentina", ORBE 21  21.2
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://dz92jh1unkapm.cloudfront.net/accounts/5cf95117cb97cae8e2c36676/logo.png" group-title="Argentina", UNIFE TV  25.1
https://dacastmmd.mmdlive.lldns.net/dacastmmd/98adedd6dec04a2d8663899b927f9383/chunklist_b4628000.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VISANTAM.png" group-title="Argentina", SANTA MARIA
http://www.trimi.com.ar/santa_maria/streaming/mystreamSantaMariaHSMed.m3u8



#EXTINF:-1 tvg-logo="http://www.tectv.gob.ar/resources/img/logo.png" group-title="Argentina", TEC TV  22.5
https://g3.mc-hor.transport.edge-access.net/a09/ngrp:gcba_video3-100042_all/gcba_video3-100042_720p.m3u8






#EXTINF:-1, CANAL 26 
http://200.115.193.177/live/26hd-720/.m3u8


'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
            pop() = None               
                return 
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
            pop() = None
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/Nicolas0919/Guia-EPG/master/GuiaEPG.xml"')

#s = requests.Session()
with open('../ARGENTINA.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
print(banner)            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    

