[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# VideoCapture

class in UnityEngine.Windows.WebCam

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Records a video from the web camera directly to disk.

This API is supported in the Windows Players (Standalone and Universal Windows
Platform) and in the Windows Editor. The final video recording will be stored
on the local file system in the MP4 format. VideoCapture is implemented using
the WinRT interface: Windows.Media.Capture.IMediaCapture.  
For more information, see Microsoft documentation on [Windows
MediaCapture](https://docs.microsoft.com/en-
us/uwp/api/Windows.Media.Capture.MediaCapture).  
  
**Note:** Universal Windows Platform requires both webcam and microphone
capabilities.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Linq;
    using UnityEngine.Windows.WebCam;  
      
    public class VideoCaptureExample : [MonoBehaviour](MonoBehaviour.html)
    {
        static readonly float MaxRecordingTime = 5.0f;  
      
        [VideoCapture](Windows.WebCam.VideoCapture.html) m_VideoCapture = null;
        float m_stopRecordingTimer = float.MaxValue;  
      
        // Use this for initialization
        void Start()
        {
            StartVideoCaptureTest();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (m_VideoCapture == null || !m_VideoCapture.IsRecording)
            {
                return;
            }  
      
            if ([Time.time](Time-time.html) > m_stopRecordingTimer)
            {
                m_VideoCapture.StopRecordingAsync(OnStoppedRecordingVideo);
            }
        }  
      
        void StartVideoCaptureTest()
        {
            [Resolution](Resolution.html) cameraResolution = VideoCapture.SupportedResolutions.OrderByDescending((res) => res.width * res.height).First();
            [Debug.Log](Debug.Log.html)(cameraResolution);  
      
            float cameraFramerate = [VideoCapture.GetSupportedFrameRatesForResolution](Windows.WebCam.VideoCapture.GetSupportedFrameRatesForResolution.html)(cameraResolution).OrderByDescending((fps) => fps).First();
            [Debug.Log](Debug.Log.html)(cameraFramerate);  
      
            [VideoCapture.CreateAsync](Windows.WebCam.VideoCapture.CreateAsync.html)(false, delegate([VideoCapture](Windows.WebCam.VideoCapture.html) videoCapture)
            {
                if (videoCapture != null)
                {
                    m_VideoCapture = videoCapture;
                    [Debug.Log](Debug.Log.html)("Created [VideoCapture](Windows.WebCam.VideoCapture.html) Instance!");  
      
                    [CameraParameters](Windows.WebCam.CameraParameters.html) cameraParameters = new [CameraParameters](Windows.WebCam.CameraParameters.html)();
                    cameraParameters.hologramOpacity = 0.0f;
                    cameraParameters.frameRate = cameraFramerate;
                    cameraParameters.cameraResolutionWidth = cameraResolution.width;
                    cameraParameters.cameraResolutionHeight = cameraResolution.height;
                    cameraParameters.pixelFormat = [CapturePixelFormat.BGRA32](Windows.WebCam.CapturePixelFormat.BGRA32.html);  
      
                    m_VideoCapture.StartVideoModeAsync(cameraParameters,
                        [VideoCapture.AudioState.ApplicationAndMicAudio](Windows.WebCam.VideoCapture.AudioState.ApplicationAndMicAudio.html),
                        OnStartedVideoCaptureMode);
                }
                else
                {
                    [Debug.LogError](Debug.LogError.html)("Failed to create [VideoCapture](Windows.WebCam.VideoCapture.html) Instance!");
                }
            });
        }  
      
        void OnStartedVideoCaptureMode(VideoCapture.VideoCaptureResult result)
        {
            [Debug.Log](Debug.Log.html)("Started Video Capture [Mode](Scripting.GarbageCollector.Mode.html)!");
            string timeStamp = Time.time.ToString().Replace(".", "").Replace(":", "");
            string filename = string.Format("TestVideo_{0}.mp4", timeStamp);
            string filepath = System.IO.Path.Combine([Application.persistentDataPath](Application-persistentDataPath.html), filename);
            filepath = filepath.Replace("/", @"\");
            m_VideoCapture.StartRecordingAsync(filepath, OnStartedRecordingVideo);
        }  
      
        void OnStoppedVideoCaptureMode(VideoCapture.VideoCaptureResult result)
        {
            [Debug.Log](Debug.Log.html)("Stopped Video Capture [Mode](Scripting.GarbageCollector.Mode.html)!");
        }  
      
        void OnStartedRecordingVideo(VideoCapture.VideoCaptureResult result)
        {
            [Debug.Log](Debug.Log.html)("Started Recording Video!");
            m_stopRecordingTimer = [Time.time](Time-time.html) + MaxRecordingTime;
        }  
      
        void OnStoppedRecordingVideo(VideoCapture.VideoCaptureResult result)
        {
            [Debug.Log](Debug.Log.html)("Stopped Recording Video!");
            m_VideoCapture.StopVideoModeAsync(OnStoppedVideoCaptureMode);
        }
    }
    

### Static Properties

[SupportedResolutions](Windows.WebCam.VideoCapture.SupportedResolutions.html)|
A list of all the supported device resolutions for recording videos.  
---|---  
  
### Properties

[IsRecording](Windows.WebCam.VideoCapture.IsRecording.html)| Indicates whether
or not the VideoCapture instance is currently recording video.  
---|---  
  
### Public Methods

[Dispose](Windows.WebCam.VideoCapture.Dispose.html)| You must call Dispose to
shutdown the VideoCapture instance and release the native WinRT objects.  
---|---  
[GetUnsafePointerToVideoDeviceController](Windows.WebCam.VideoCapture.GetUnsafePointerToVideoDeviceController.html)|
Provides a COM pointer to the native IVideoDeviceController.  
[StartRecordingAsync](Windows.WebCam.VideoCapture.StartRecordingAsync.html)|
Asynchronously records a video from the web camera to the file system.  
[StartVideoModeAsync](Windows.WebCam.VideoCapture.StartVideoModeAsync.html)|
Asynchronously starts video mode.  
[StopRecordingAsync](Windows.WebCam.VideoCapture.StopRecordingAsync.html)|
Asynchronously stops recording a video from the web camera to the file system.  
[StopVideoModeAsync](Windows.WebCam.VideoCapture.StopVideoModeAsync.html)|
Asynchronously stops video mode.  
  
### Static Methods

[CreateAsync](Windows.WebCam.VideoCapture.CreateAsync.html)| Asynchronously
creates an instance of a VideoCapture object that can be used to record videos
from the web camera to disk.  
---|---  
[GetSupportedFrameRatesForResolution](Windows.WebCam.VideoCapture.GetSupportedFrameRatesForResolution.html)|
Returns the supported frame rates at which a video can be recorded given a
resolution.  
  
### Delegates

[OnStartedRecordingVideoCallback](Windows.WebCam.VideoCapture.OnStartedRecordingVideoCallback.html)|
Called when the web camera begins recording the video.  
---|---  
[OnStoppedRecordingVideoCallback](Windows.WebCam.VideoCapture.OnStoppedRecordingVideoCallback.html)|
Called when the video recording has been saved to the file system.  
[OnVideoCaptureResourceCreatedCallback](Windows.WebCam.VideoCapture.OnVideoCaptureResourceCreatedCallback.html)|
Called when a VideoCapture resource has been created.  
[OnVideoModeStartedCallback](Windows.WebCam.VideoCapture.OnVideoModeStartedCallback.html)|
Called when video mode has been started.  
[OnVideoModeStoppedCallback](Windows.WebCam.VideoCapture.OnVideoModeStoppedCallback.html)|
Called when video mode has been stopped.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

