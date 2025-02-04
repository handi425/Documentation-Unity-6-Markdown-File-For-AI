[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/time-capture-frame-rate.html)
  * [中文](/cn/current/Manual/time-capture-frame-rate.html)
  * [日本語](/ja/current/Manual/time-capture-frame-rate.html)
  * [한국어](/kr/current/Manual/time-capture-frame-rate.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/time-capture-frame-rate.html)
  * [中文](/cn/current/Manual/time-capture-frame-rate.html)
  * [日本語](/ja/current/Manual/time-capture-frame-rate.html)
  * [한국어](/kr/current/Manual/time-capture-frame-rate.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Managing time and frame rate](managing-time-and-frame-rate.html)
  * Capturing frame rate

[](time-scale.html)

In-game time and real time

[](instantiating-prefabs.html)

Instantiating prefabs at runtime

# Capturing frame rate

A special case of time management is where you want to record gameplay as a
video. Since the task of saving screen images takes considerable time, the
game’s normal frame rate is reduced, and the video doesn’t reflect the game’s
true performance.

To improve the video’s appearance, use the [Capture
Framerate](../ScriptReference/Time-captureFramerate.html) property. The
property’s default value is 0, for unrecorded gameplay. When you set the
property’s value to anything other than zero, game time is slowed and the
frame updates are issued at precise regular intervals for the purposes of
recording. The interval between frames is equal to `1 /
Time.captureFramerate`, so if you set the value to 5.0 then updates occur
every fifth of a second. With the demands on frame rate effectively reduced,
you have time in the Update function to save screenshots or take other
actions:

    
    
    //C# script example
    using UnityEngine;
    using System.Collections;
    
    public class ExampleScript : MonoBehaviour {
        // Capture frames as a screenshot sequence. Images are
        // stored as PNG files in a folder - these can be combined into
        // a movie using image utility software (eg, QuickTime Pro).
        // The folder to contain our screenshots.
        // If the folder exists we will append numbers to create an empty folder.
        string folder = "ScreenshotFolder";
        int frameRate = 25;
            
        void Start () {
            // Set the playback frame rate (real time will not relate to game time after this).
            Time.captureFramerate = frameRate;
            
            // Create the folder
            System.IO.Directory.CreateDirectory(folder);
        }
        
        void Update () {
            // Append filename to folder name (format is '0005 shot.png"')
            string name = string.Format("{0}/{1:D04} shot.png", folder, Time.frameCount );
            
            // Capture the screenshot to the specified file.
            Application.CaptureScreenshot(name);
        }
    }
    

Using this technique improves the video, but can make the game much harder to
play. Try different values of Time.captureFramerate to find a good balance.

## Additional resources

  * [Time.captureFramerate API reference](../ScriptReference/Time-captureFramerate.html)

[](time-scale.html)

In-game time and real time

[](instantiating-prefabs.html)

Instantiating prefabs at runtime

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

