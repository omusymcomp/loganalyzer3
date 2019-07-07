# -*- coding: utf-8 -*-
#! /usr/bin/env python

from lib import lib_log_analyzer as lib

def saveKickDistribution( feat ):

    with open( 'kick_distribution.csv', 'a' ) as f:

        f_left = open("kick_distribution_left.csv", "a")
        f_right = open("kick_distribution_right.csv", "a")
        f_front = open("kick_distribution_front.csv", "a")
        f_back = open("kick_distribution_back.csv", "a")
        f_success = open("kick_distribution_success.csv", "a")

        for i in range( len( feat.kick_sequence ) - 1 ):
            # if not terminal condition
            if ( feat.kick_sequence[i][4] != -1 \
                 and feat.kick_sequence[i+1][4] != 0 ):
                f.write( str( feat.kick_sequence[i][1] ) + ',' +
                         str( feat.kick_sequence[i][2] ) + ',' +
                         str( lib.calcDistC( feat.kick_sequence[i][1],
                                             feat.kick_sequence[i][2],
                                             feat.kick_sequence[i+1][1],
                                             feat.kick_sequence[i+1][2] ) ) +
                         str('\n') )

                if (feat.kick_sequence[i][3] == 1):
                    f_success.write( str( feat.kick_sequence[i][1] ) + ',' +
                             str( feat.kick_sequence[i][2] ) + ',' +
                             str( lib.calcDistC( feat.kick_sequence[i][1],
                                                 feat.kick_sequence[i][2],
                                                 feat.kick_sequence[i+1][1],
                                                 feat.kick_sequence[i+1][2] ) ) +
                             str('\n') )

                degree = lib.changeRadianToDegree(lib.calcRadianC(feat.kick_sequence[i][1], feat.kick_sequence[i][2],
                                                                  feat.kick_sequence[i+1][1], feat.kick_sequence[i+1][2]))
                if (degree > -45.0 and degree <= 45.0):
                    f_front.write( str( feat.kick_sequence[i][1] ) + ',' +
                                   str( feat.kick_sequence[i][2] ) + ',' +
                                   str( lib.calcDistC( feat.kick_sequence[i][1],
                                                       feat.kick_sequence[i][2],
                                                       feat.kick_sequence[i+1][1],
                                                       feat.kick_sequence[i+1][2] ) ) +
                                   str('\n') )
                elif (degree > 45.0 and degree <= 135.0):
                    f_right.write( str( feat.kick_sequence[i][1] ) + ',' +
                                   str( feat.kick_sequence[i][2] ) + ',' +
                                   str( lib.calcDistC( feat.kick_sequence[i][1],
                                                       feat.kick_sequence[i][2],
                                                       feat.kick_sequence[i+1][1],
                                                       feat.kick_sequence[i+1][2] ) ) +
                                   str('\n') )
                elif (degree > 135.0 or degree <= -135.0):
                    f_back.write( str( feat.kick_sequence[i][1] ) + ',' +
                                  str( feat.kick_sequence[i][2] ) + ',' +
                                  str( lib.calcDistC( feat.kick_sequence[i][1],
                                                      feat.kick_sequence[i][2],
                                                      feat.kick_sequence[i+1][1],
                                                      feat.kick_sequence[i+1][2] ) ) +
                                   str('\n') )
                elif( degree > -135.0 and degree <= -45.0 ):
                    f_left.write( str( feat.kick_sequence[i][1] ) + ',' +
                                  str( feat.kick_sequence[i][2] ) + ',' +
                                  str( lib.calcDistC( feat.kick_sequence[i][1],
                                                      feat.kick_sequence[i][2],
                                                      feat.kick_sequence[i+1][1],
                                                      feat.kick_sequence[i+1][2] ) ) +
                                   str('\n') )


        f_left.close()
        f_right.close()
        f_front.close()
        f_back.close()
        f_success.close()

def printKickDistribution( sp, feat ):

    import matplotlib
    matplotlib.use('Agg')
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.patches import Circle
    import mpl_toolkits.mplot3d.art3d as art3d
    from matplotlib import pyplot as plt
    import matplotlib.font_manager as fm

    xlim = sp.pitch_length / 2 + 5.0
    ylim = sp.pitch_width / 2 + 5.0
    fm._rebuild()
    #plt.rc('font', family='Times New Roman')
    #plt.rcParams['font.family'] = 'Times New Roman'

    fig = plt.figure(figsize=(10.5, 6.8))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    ax = fig.add_subplot( 111, projection='3d', azim = 240 )

    ax.set_xlabel("{\it x}", fontsize=32, labelpad=20)
    ax.set_ylabel("{\it y}", fontsize=32, labelpad=20)
    ax.set_zlabel("{\it distance}", fontsize=32, labelpad=20)

    ax.set_xlim( -xlim, xlim )
    ax.set_ylim( ylim, -ylim )

    ax.tick_params(labelsize=32, pad=10)

    # plot soccer fields
    ax.plot3D( [ sp.goal_line_l, -sp.penalty_area_x ], [ -sp.penalty_area_y, -sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_l, -sp.penalty_area_x ], [ sp.penalty_area_y, sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_r, sp.penalty_area_x ], [ -sp.penalty_area_y, -sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_r, sp.penalty_area_x ], [ sp.penalty_area_y, sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ -sp.penalty_area_x, -sp.penalty_area_x ], [ sp.penalty_area_y, -sp.penalty_area_y ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.penalty_area_x, sp.penalty_area_x ], [ sp.penalty_area_y, -sp.penalty_area_y ],[ 0, 0 ], color='g', linewidth=4 )

    ax.plot3D( [ sp.goal_line_l, sp.goal_line_r ], [ -sp.pitch_width / 2, -sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_l, sp.goal_line_r ], [ sp.pitch_width / 2, sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_l, sp.goal_line_l ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )
    ax.plot3D( [ sp.goal_line_r, sp.goal_line_r ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], [ 0, 0 ], color='g', linewidth=4 )

    plt.plot( [ 0, 0 ], [  -sp.pitch_width / 2, sp.pitch_width / 2 ], color='g', linewidth=4 )

    p = Circle((0.5, 0.5), 9, ec="g", fc="None", linewidth=4 )
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=0.0, zdir="z")

    # plot kick distribution
    for i in range( len( feat.kick_sequence ) - 1 ):
        # if not tarminal condition
        if ( feat.kick_sequence[i][4] != -1 \
             and feat.kick_sequence[i+1][4] != 0 ):
            ax.plot3D( [ feat.kick_sequence[i][1], feat.kick_sequence[i][1] ],
                       [ feat.kick_sequence[i][2], feat.kick_sequence[i][2] ],
                       [ 0,  lib.calcDistC( feat.kick_sequence[i][1],
                                            feat.kick_sequence[i][2],
                                            feat.kick_sequence[i+1][1],
                                            feat.kick_sequence[i+1][2] ) ],
                       "red" )

    filename = feat.team_point[0] + "-kick_distribution"
    extension = [".eps", ".pdf", ".png", ".svg"]
    for e in extension:
        plt.savefig(filename+e, dpi=300, bbox_inches="tight", transparent=True)
    #plt.show()