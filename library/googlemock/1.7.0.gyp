{
    "targets": [
        {
            "target_name": "googlemock",
            "type": "static_library",
            "include_dirs": [
                "1.7.0/gmock-1.7.0/include",
                "1.7.0/gmock-1.7.0" # needed for gmock-all.cc
            ],
            "sources": [
                # here we cannot reference *.cc since the src dir contains
                # the funky gmock-all.cc which #includes everything. Of course
                # we can just reference this gmock-all.cc here:
                "1.7.0/gmock-1.7.0/src/gmock-all.cc"
            ],
            "dependencies": [
                "../googletest/googletest.gyp:*"
            ],
            "direct_dependent_settings": {
                "include_dirs": [
                    "1.7.0/gmock-1.7.0/include"
                    # 1.7.0/gmock-1.7.0[/src] is not in here on purpose
                ]
            }
        },

        {
            "target_name": "googlemock_test",
            "type": "executable",
            #"include_dirs": [
            #    # only needed because gmock_all_test.cc includes other
            #    # files from test/ via #include "test/foo.cc"
            #    "1.7.0/gmock-1.7.0"
            #],
            "sources": [ 
                # the 'all' test compiled several minutes, so instead lets
                # compile a smaller/faster test:
                #"1.7.0/gmock-1.7.0/test/gmock_all_test.cc"

                "1.7.0/gmock-1.7.0/test/gmock_test.cc"
            ],
            "dependencies": [
                "googlemock",
                "../googletest/googletest.gyp:*"
            ]
        }
    ]
}