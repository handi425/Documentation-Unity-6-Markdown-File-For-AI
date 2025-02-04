[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/VideoPlayer-MigratingFromMovieTexture.html)
  * [中文](/cn/current/Manual/VideoPlayer-MigratingFromMovieTexture.html)
  * [日本語](/ja/current/Manual/VideoPlayer-MigratingFromMovieTexture.html)
  * [한국어](/kr/current/Manual/VideoPlayer-MigratingFromMovieTexture.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/VideoPlayer-MigratingFromMovieTexture.html)
  * [中文](/cn/current/Manual/VideoPlayer-MigratingFromMovieTexture.html)
  * [日本語](/ja/current/Manual/VideoPlayer-MigratingFromMovieTexture.html)
  * [한국어](/kr/current/Manual/VideoPlayer-MigratingFromMovieTexture.html)

  * [Video and cutscenes](Video.html)
  * [Video Player](VideoPlayer.html)
  * Migrating from MovieTexture to VideoPlayer

[](class-VideoPlayer.html)

Video Player component

[](video-clock.html)

Clock management with the Video Player component

# Migrating from MovieTexture to VideoPlayer

If you have projects that use the legacy [MovieTexture](class-
MovieTexture.html) component to download and play movies, you can update them
to use the newer [VideoPlayer](class-VideoPlayer.html) component.

To help you migrate from MovieTexture to VideoPlayer, this page provides
examples of how to download and play back a movie using each component.

## Playing a Movie

### MovieTexture

    
    
    using UnityEngine;
    
    public class PlayMovieMT : MonoBehaviour
    {
        public AudioClip movieAudioClip;
        public MovieTexture movieTexture;
    
        void Start()
        {
            var audioSource = gameObject.AddComponent<AudioSource>();
            audioSource.clip = movieAudioClip;
        }
    
        void Update()
        {
            if (Input.GetButtonDown("Jump"))
            {
                var audioSource = GetComponent<AudioSource>();
                GetComponent<Renderer>().material.mainTexture = movieTexture;
    
                if (movieTexture.isPlaying)
                {
                    movieTexture.Pause();
                    audioSource.Pause();
                }
                else
                {
                    movieTexture.Play();
                    audioSource.Play();
                }
            }
        }
    }
    

### VideoPlayer

    
    
    using UnityEngine;
    
    public class PlayMovieVP : MonoBehaviour
    {
        public UnityEngine.Video.VideoClip videoClip;
    
        void Start()
        {
            var videoPlayer = gameObject.AddComponent<UnityEngine.Video.VideoPlayer>();
            var audioSource = gameObject.AddComponent<AudioSource>();
    
            videoPlayer.playOnAwake = false;
            videoPlayer.clip = videoClip;
            videoPlayer.renderMode = UnityEngine.Video.VideoRenderMode.MaterialOverride;
            videoPlayer.targetMaterialRenderer = GetComponent<Renderer>();
            videoPlayer.targetMaterialProperty = "_MainTex";
            videoPlayer.audioOutputMode = UnityEngine.Video.VideoAudioOutputMode.AudioSource;
            videoPlayer.SetTargetAudioSource(0, audioSource);
        }
    
        void Update()
        {
            if (Input.GetButtonDown("Jump"))
            {
                var vp = GetComponent<UnityEngine.Video.VideoPlayer>();
    
                if (vp.isPlaying)
                {
                    vp.Pause();
                }
                else
                {
                    vp.Play();
                }
            }
        }
    }
    

## Downloading a Movie

### MovieTexture

    
    
    using UnityEngine;
    
    public class DownloadMovieMT : MonoBehaviour
    {
        void Start()
        {
            StartCoroutine(GetMovieTexture());
        }
    
        IEnumerator GetMovieTexture()
        {
            using (var uwr = UnityWebRequestMultimedia.GetMovieTexture("https://myserver.com/mymovie.ogv"))
            {
                yield return uwr.SendWebRequest();
                if (uwr.isNetworkError || uwr.isHttpError)
                {
                    Debug.LogError(uwr.error);
                    yield break;
                }
    
                MovieTexture movie = DownloadHandlerMovieTexture.GetContent(uwr);
    
                GetComponent<Renderer>().material.mainTexture = movie;
                movie.loop = true;
                movie.Play();
            }
        }
    }
    

### VideoPlayer

    
    
    using UnityEngine;
    
    public class DownloadMovieVP : MonoBehaviour
    {
        void Start()
        {
            var vp = gameObject.AddComponent<UnityEngine.Video.VideoPlayer>();
            vp.url = "https://myserver.com/mymovie.mp4";
    
            vp.isLooping = true;
            vp.renderMode = UnityEngine.Video.VideoRenderMode.MaterialOverride;
            vp.targetMaterialRenderer = GetComponent<Renderer>();
            vp.targetMaterialProperty = "_MainTex";
    
            vp.Play();
        }
    }
    

* * *

  * 2019–05–07 Page published 

[](class-VideoPlayer.html)

Video Player component

[](video-clock.html)

Clock management with the Video Player component

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

