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

#  [Time](Time.html).captureDeltaTime

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

public static float captureDeltaTime;

### Description

Slows your application’s playback time to allow Unity to save screenshots in
between frames.

If this property has a non-zero value then [Time.time](Time-time.html)
increases at an interval of captureDeltaTime (scaled by [Time.timeScale](Time-
timeScale.html)) regardless of real time and the duration of a frame. This is
useful if you want to capture a movie where you need a constant frame rate and
want to leave enough time between frames to save screen images.  
  
**Note:** captureDeltaTime does not have any affect on
[Time.unscaledTime](Time-unscaledTime.html). Therefore, if parts of your
application rely on it for animations or other effects, captureDeltaTime might
not be enough to capture a movie.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Capture frames as a screenshot sequence. Images are
    // stored as PNG files in a folder - these can be combined into
    // a movie using image utility software (eg, QuickTime Pro).  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // The folder to contain our screenshots.
        // If the folder exists we will append numbers to create an empty folder.
        public string folder = "ScreenshotFolder";
        public int frameRate = 25;
        void Start()
        {
            // Set the playback framerate (real time will not relate to game time after this).
            [Time.captureDeltaTime](Time-captureDeltaTime.html) = 1.0f / frameRate;  
      
            // Create the folder
            System.IO.Directory.CreateDirectory(folder);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // Append filename to folder name (format is '0005 shot.png"')
            string name = string.Format("{0}/{1:D04} shot.png", folder, [Time.frameCount](Time-frameCount.html));  
      
            // Capture the screenshot to the specified file.
            [ScreenCapture.CaptureScreenshot](ScreenCapture.CaptureScreenshot.html)(name);
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

