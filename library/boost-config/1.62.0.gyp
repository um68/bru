{
    "targets": [
        {
            "target_name": "boost-config",
            "type": "none",
            "include_dirs": [
                "1.62.0/config-boost-1.62.0/include"
            ],
            "all_dependent_settings": {
                "defines": [
                  # The Boost auto-link #pragma lib is neat in general, but 
                  # doesn't work well with these *.gyp files here since the
                  # library file names generated by gyp don't match what Boost's
                  # auto-link.hpp expects (even when using BOOST_AUTO_LINK_NOMANGLE)
                  # So let's just disable this mechanism, bru takes care of library
                  # deps already anyway.
                  "BOOST_ALL_NO_LIB"
                ],
                "include_dirs": [
                    "1.62.0/config-boost-1.62.0/include"
                ]
            }
        }
    ]
}