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

#  [EditorWindow](EditorWindow.html).OnGUI()

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

Implement your own editor GUI here.

![](../StaticFiles/ScriptRefImages/SimpleRecorder.png)  
_Use OnGUI to draw all the controls of your window._

    
    
    // A simple script that saves frames from the Game view when in Play mode.
    //
    // You can put the frames together later to create a video.
    // The frames are saved in the project, at the same level of the project hierarchy as the Assets folder.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SimpleRecorder : [EditorWindow](EditorWindow.html)
    {
        string fileName = "FileName";  
      
        string status = "Idle";
        string recordButton = "Record";
        bool recording = false;
        float lastFrameTime = 0.0f;
        int capturedFrame = 0;  
      
        [[MenuItem](MenuItem.html)("Example/Simple [Recorder](Profiling.Recorder.html)")]
        static void Init()
        {
            SimpleRecorder window =
                (SimpleRecorder)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(SimpleRecorder));
        }  
      
        void OnGUI()
        {
            fileName = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("[File](Windows.File.html) Name:", fileName);  
      
            if ([GUILayout.Button](GUILayout.Button.html)(recordButton))
            {
                if (recording)  //recording
                {
                    status = "Idle...";
                    recordButton = "Record";
                    recording = false;
                }
                else     // idle
                {
                    capturedFrame = 0;
                    recordButton = "Stop";
                    recording = true;
                }
            }
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("[Status](TouchScreenKeyboard.Status.html): ", status);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (recording)
            {
                if ([EditorApplication.isPlaying](EditorApplication-isPlaying.html) && ![EditorApplication.isPaused](EditorApplication-isPaused.html))
                {
                    RecordImages();
                    Repaint();
                }
                else
                    status = "Waiting for [Editor](Editor.html) to Play";
            }
        }  
      
        void RecordImages()
        {
            if (lastFrameTime < [Time.time](Time-time.html) + (1 / 24f)) // 24fps
            {
                status = "Captured frame " + capturedFrame;
                [ScreenCapture.CaptureScreenshot](ScreenCapture.CaptureScreenshot.html)(fileName + " " + capturedFrame + ".png");
                capturedFrame++;
                lastFrameTime = [Time.time](Time-time.html);
            }
        }
    }
    

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

