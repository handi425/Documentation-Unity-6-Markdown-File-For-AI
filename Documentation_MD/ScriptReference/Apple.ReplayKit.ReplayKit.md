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

**Method group is Obsolete**  

# ReplayKit

class in UnityEngine.Apple.ReplayKit

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

**Obsolete** ReplayKit will be removed in future version of Unity.

### Description

ReplayKit is only available on certain iPhone, iPad and iPod Touch devices
running iOS 9.0 or later.

ReplayKit allows you to record the audio and video of your game, along with
user commentary through the microphone and user video through the camera.
Start a recording with the StartRecording() function, and stop it with
StopRecording(). You can preview the recording with the Preview() function,
which launches a separate video viewer. In addition to local recordings, you
can broadcast your recordings via StartBroadcasting(). There are also
functions to pause, resume, and stop broadcasting.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    #if PLATFORM_IOS
    using UnityEngine.iOS;
    using UnityEngine.Apple.ReplayKit;  
      
    public class Replay : [MonoBehaviour](MonoBehaviour.html)
    {
        public bool enableMicrophone = false;
        public bool enableCamera = false;  
      
        string lastError = "";
        void OnGUI()
        {
            if (!ReplayKit.APIAvailable)
            {
                return;
            }
            var recording = ReplayKit.isRecording;
            string caption = recording ? "Stop Recording" : "Start Recording";
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 500, 200), caption))
            {
                try
                {
                    recording = !recording;
                    if (recording)
                    {
                        ReplayKit.StartRecording(enableMicrophone, enableCamera);
                    }
                    else
                    {
                        ReplayKit.StopRecording();
                    }
                }
                catch (Exception e)
                {
                    lastError = e.ToString();
                }
            }  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 220, 500, 50), "Last error: " + ReplayKit.lastError);
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 280, 500, 50), "Last exception: " + lastError);  
      
            if (ReplayKit.recordingAvailable)
            {
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 350, 500, 200), "Preview"))
                {
                    ReplayKit.Preview();
                }
                if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 560, 500, 200), "Discard"))
                {
                    ReplayKit.Discard();
                }
            }
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // If the camera is enabled, show the recorded video overlaying the game.
            if (ReplayKit.isRecording && enableCamera)
                ReplayKit.ShowCameraPreviewAt(10, 350, 200, 200);
            else
                ReplayKit.HideCameraPreview();
        }
    }
    #endif
    

### Static Methods

[StartBroadcasting](Apple.ReplayKit.ReplayKit.StartBroadcasting.html)|
Initiates and starts a new broadcast When StartBroadcast is called, user is
presented with a broadcast provider selection screen, and then a broadcast
setup screen. Once it is finished, a broadcast will be started, and the
callback will be invoked. It will also be invoked in case of any error.  
---|---  
  
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

