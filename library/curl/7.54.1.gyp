{
    "targets": [
        {
            "target_name": "curl",
            "type": "static_library",
            "include_dirs": [
                                "7.54.1/curl-7.54.1/include",
                                "7.54.1/curl-7.54.1/lib"
            ],
            "defines": [
                # from vcproj
                "BUILDING_LIBCURL",
                "CURL_STATICLIB",

                "CURL_DISABLE_LDAP", # unless we'd care about querying ldap://
                # Should we disabled other rarely used features? See
                # http://stackoverflow.com/questions/24102240/minimal-curl-cross-compile-for-windows

                # SSL is needed for HTTPS requests, instead of openssl curl
                # optionally could use native windows libs?
                "USE_SSLEAY",
                "USE_OPENSSL"

                # not: "USE_LIBSSH2"
                # What would libssh2 provide? Only sftp support I think.
            ],
            "conditions": [
                ["OS=='linux'", {
                    "defines": [
                        "HAVE_CONFIG_H"
                    ]
                }],
				["OS=='iOS'", {
                    "defines": [
                        "HAVE_CONFIG_H"
                    ]
                }],
				["OS=='mac'", {
                    "defines": [
                        "HAVE_CONFIG_H"
                    ]
                }]


            ],
            # sources list generated for Windows build via
            # ~\bru\vcproj2gyp.py 7.54.1/curl-7.54.1/projects/Windows/VC11/lib/libcurl.vcxproj "LIB Release - LIB OpenSSL" Win32
            # TODO: only was verified to work on Windows, make it work on Linux also.
            "sources": [                            "7.54.1/curl-7.54.1/lib/amigaos.c",
                "7.54.1/curl-7.54.1/lib/asyn-ares.c",
                "7.54.1/curl-7.54.1/lib/asyn-thread.c",
                "7.54.1/curl-7.54.1/lib/base64.c",
                "7.54.1/curl-7.54.1/lib/conncache.c",
                "7.54.1/curl-7.54.1/lib/connect.c",
                "7.54.1/curl-7.54.1/lib/content_encoding.c",
                "7.54.1/curl-7.54.1/lib/cookie.c",
                "7.54.1/curl-7.54.1/lib/curl_addrinfo.c",
                "7.54.1/curl-7.54.1/lib/curl_des.c",
                "7.54.1/curl-7.54.1/lib/curl_endian.c",
                "7.54.1/curl-7.54.1/lib/curl_fnmatch.c",
                "7.54.1/curl-7.54.1/lib/curl_gethostname.c",
                "7.54.1/curl-7.54.1/lib/curl_gssapi.c",
                "7.54.1/curl-7.54.1/lib/curl_memrchr.c",
                "7.54.1/curl-7.54.1/lib/curl_multibyte.c",
                "7.54.1/curl-7.54.1/lib/curl_ntlm_core.c",
                "7.54.1/curl-7.54.1/lib/curl_ntlm_wb.c",
                "7.54.1/curl-7.54.1/lib/curl_rtmp.c",
                "7.54.1/curl-7.54.1/lib/curl_sasl.c",
                "7.54.1/curl-7.54.1/lib/curl_sspi.c",
                "7.54.1/curl-7.54.1/lib/curl_threads.c",
                "7.54.1/curl-7.54.1/lib/dict.c",
                "7.54.1/curl-7.54.1/lib/dotdot.c",
                "7.54.1/curl-7.54.1/lib/easy.c",
                "7.54.1/curl-7.54.1/lib/escape.c",
                "7.54.1/curl-7.54.1/lib/file.c",
                "7.54.1/curl-7.54.1/lib/fileinfo.c",
                "7.54.1/curl-7.54.1/lib/formdata.c",
                "7.54.1/curl-7.54.1/lib/ftp.c",
                "7.54.1/curl-7.54.1/lib/ftplistparser.c",
                "7.54.1/curl-7.54.1/lib/getenv.c",
                "7.54.1/curl-7.54.1/lib/getinfo.c",
                "7.54.1/curl-7.54.1/lib/gopher.c",
                "7.54.1/curl-7.54.1/lib/hash.c",
                "7.54.1/curl-7.54.1/lib/hmac.c",
                "7.54.1/curl-7.54.1/lib/hostasyn.c",
                "7.54.1/curl-7.54.1/lib/hostcheck.c",
                "7.54.1/curl-7.54.1/lib/hostip.c",
                "7.54.1/curl-7.54.1/lib/hostip4.c",
                "7.54.1/curl-7.54.1/lib/hostip6.c",
                "7.54.1/curl-7.54.1/lib/hostsyn.c",
                "7.54.1/curl-7.54.1/lib/http.c",
                "7.54.1/curl-7.54.1/lib/http2.c",
                "7.54.1/curl-7.54.1/lib/http_chunks.c",
                "7.54.1/curl-7.54.1/lib/http_digest.c",
                "7.54.1/curl-7.54.1/lib/http_negotiate.c",
                "7.54.1/curl-7.54.1/lib/http_ntlm.c",
                "7.54.1/curl-7.54.1/lib/http_proxy.c",
                "7.54.1/curl-7.54.1/lib/idn_win32.c",
                "7.54.1/curl-7.54.1/lib/if2ip.c",
                "7.54.1/curl-7.54.1/lib/imap.c",
                "7.54.1/curl-7.54.1/lib/inet_ntop.c",
                "7.54.1/curl-7.54.1/lib/inet_pton.c",
                "7.54.1/curl-7.54.1/lib/krb5.c",
                "7.54.1/curl-7.54.1/lib/ldap.c",
                "7.54.1/curl-7.54.1/lib/llist.c",
                "7.54.1/curl-7.54.1/lib/md4.c",
                "7.54.1/curl-7.54.1/lib/md5.c",
                "7.54.1/curl-7.54.1/lib/memdebug.c",
                "7.54.1/curl-7.54.1/lib/mprintf.c",
                "7.54.1/curl-7.54.1/lib/multi.c",
                "7.54.1/curl-7.54.1/lib/netrc.c",
                "7.54.1/curl-7.54.1/lib/non-ascii.c",
                "7.54.1/curl-7.54.1/lib/nonblock.c",
                "7.54.1/curl-7.54.1/lib/nwlib.c",
                "7.54.1/curl-7.54.1/lib/nwos.c",
                "7.54.1/curl-7.54.1/lib/openldap.c",
                "7.54.1/curl-7.54.1/lib/parsedate.c",
                "7.54.1/curl-7.54.1/lib/pingpong.c",
                "7.54.1/curl-7.54.1/lib/pipeline.c",
                "7.54.1/curl-7.54.1/lib/pop3.c",
                "7.54.1/curl-7.54.1/lib/progress.c",
                "7.54.1/curl-7.54.1/lib/rand.c",
                "7.54.1/curl-7.54.1/lib/rtsp.c",
                "7.54.1/curl-7.54.1/lib/security.c",
                "7.54.1/curl-7.54.1/lib/select.c",
                "7.54.1/curl-7.54.1/lib/sendf.c",
                "7.54.1/curl-7.54.1/lib/share.c",
                "7.54.1/curl-7.54.1/lib/slist.c",
                "7.54.1/curl-7.54.1/lib/smb.c",
                "7.54.1/curl-7.54.1/lib/smtp.c",
                "7.54.1/curl-7.54.1/lib/socks.c",
                "7.54.1/curl-7.54.1/lib/socks_gssapi.c",
                "7.54.1/curl-7.54.1/lib/socks_sspi.c",
                "7.54.1/curl-7.54.1/lib/speedcheck.c",
                "7.54.1/curl-7.54.1/lib/splay.c",
                "7.54.1/curl-7.54.1/lib/ssh.c",
                "7.54.1/curl-7.54.1/lib/strcase.c",
                "7.54.1/curl-7.54.1/lib/strdup.c",
                "7.54.1/curl-7.54.1/lib/strerror.c",
                "7.54.1/curl-7.54.1/lib/strtok.c",
                "7.54.1/curl-7.54.1/lib/strtoofft.c",
                "7.54.1/curl-7.54.1/lib/system_win32.c",
                "7.54.1/curl-7.54.1/lib/telnet.c",
                "7.54.1/curl-7.54.1/lib/tftp.c",
                "7.54.1/curl-7.54.1/lib/timeval.c",
                "7.54.1/curl-7.54.1/lib/transfer.c",
                "7.54.1/curl-7.54.1/lib/url.c",
                "7.54.1/curl-7.54.1/lib/version.c",
                "7.54.1/curl-7.54.1/lib/warnless.c",
                "7.54.1/curl-7.54.1/lib/wildcard.c",
                "7.54.1/curl-7.54.1/lib/x509asn1.c",
                "7.54.1/curl-7.54.1/lib/vauth/cleartext.c",
                "7.54.1/curl-7.54.1/lib/vauth/cram.c",
                "7.54.1/curl-7.54.1/lib/vauth/digest.c",
                "7.54.1/curl-7.54.1/lib/vauth/digest_sspi.c",
                "7.54.1/curl-7.54.1/lib/vauth/krb5_gssapi.c",
                "7.54.1/curl-7.54.1/lib/vauth/krb5_sspi.c",
                "7.54.1/curl-7.54.1/lib/vauth/ntlm.c",
                "7.54.1/curl-7.54.1/lib/vauth/ntlm_sspi.c",
                "7.54.1/curl-7.54.1/lib/vauth/oauth2.c",
                "7.54.1/curl-7.54.1/lib/vauth/spnego_gssapi.c",
                "7.54.1/curl-7.54.1/lib/vauth/spnego_sspi.c",
                "7.54.1/curl-7.54.1/lib/vauth/vauth.c",
                "7.54.1/curl-7.54.1/lib/vtls/axtls.c",
                "7.54.1/curl-7.54.1/lib/vtls/cyassl.c",
                "7.54.1/curl-7.54.1/lib/vtls/darwinssl.c",
                "7.54.1/curl-7.54.1/lib/vtls/gskit.c",
                "7.54.1/curl-7.54.1/lib/vtls/gtls.c",
                "7.54.1/curl-7.54.1/lib/vtls/mbedtls.c",
                "7.54.1/curl-7.54.1/lib/vtls/nss.c",
                "7.54.1/curl-7.54.1/lib/vtls/openssl.c",
                "7.54.1/curl-7.54.1/lib/vtls/polarssl.c",
                "7.54.1/curl-7.54.1/lib/vtls/polarssl_threadlock.c",
                "7.54.1/curl-7.54.1/lib/vtls/schannel.c",
                "7.54.1/curl-7.54.1/lib/vtls/vtls.c"
            ],
            "direct_dependent_settings": {
                "defines": [
                    "CURL_STATICLIB" # otherwise declspec import link err on windows
                ],
                "include_dirs": [
                                    "7.54.1/curl-7.54.1/include"
                ]
            },
            "dependencies": [
                "../openssl/openssl.gyp:*" # only needed for https GETs
            ]
        },

        {
            "target_name": "curl_example_https",
            "type" : "executable",
            "defines": [
                # otherwise cert verify will fail
                "SKIP_PEER_VERIFICATION"
            ],
            "test": {},
            "sources" : [
                                "7.54.1/curl-7.54.1/docs/examples/https.c"
            ],
            "dependencies" : [
                "curl"
            ],
            # this disables building the example on iOS
            "conditions": [
              ["OS=='iOS'", {
                "type": "none"
              }]
            ]
        }
    ]
}
