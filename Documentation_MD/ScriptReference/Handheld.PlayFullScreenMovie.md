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

#  [Handheld](Handheld.html).PlayFullScreenMovie

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

## Declaration

public static bool PlayFullScreenMovie(string path, [Color](Color.html)
bgColor = Color.black,
[FullScreenMovieControlMode](FullScreenMovieControlMode.html) controlMode =
FullScreenMovieControlMode.Full,
[FullScreenMovieScalingMode](FullScreenMovieScalingMode.html) scalingMode =
FullScreenMovieScalingMode.AspectFit);

### Parameters

path | Filesystem path to the movie file.  
---|---  
bgColor | Background color.  
controlMode | How the playback controls are to be displayed.  
scalingMode | How the movie is to be scaled to fit the screen.  
  
### Description

Plays a full-screen movie.

The Player streams the movie directly from device storage. It's recommended to
provide the movie as a separate file, not as a usual asset. Create a folder
named `StreamingAssets` in the Assets folder of your Unity project to store
your movie files. Unity automatically copies contents of that folder into the
application bundle.  
  
Calling this function will pause Unity during movie playback. Unity resumes
after the playback finishes.  
  
The first parameter `path` can be a network-based URL. The function detects it
by looking for a `://` substring that follows the protocol name.  
  
**iOS:** `Handheld.PlayFullScreenMovie` internally uses
`MPMoviePlayerController` object to play movies. Therefore, you should expect
the same behavior and the same supported formats. `MPMoviePlayerController`
supports any movie or audio files that already play correctly on an iPod or
iPhone.  
  
The movie files with .mov, .mp4, .mpv, and .3gp extensions and using one of
the following compression standards are supported:

  * H.264 Baseline Profile Level 3.0 video, up to 640 x 480 at 30 fps. Note that B frames are not supported in the Baseline profile.
  * MPEG-4 Part 2 video (Simple Profile).

Calling this function initiates a transition that fades the screen from your
current content to the designated background color of the Player. When
playback finishes, the Player uses another fade effect to transition back to
your content.  
  
For more information, refer to Apple's documentation on
[MPMoviePlayerController Class
Reference](http://developer.apple.com/library/ios/#DOCUMENTATION/MediaPlayer/Reference/MPMoviePlayerController_Class/Reference/Reference.html).  
  
**UWP:** On Universal Windows Platform, `Handheld.PlayFullScreenMovie`
internally uses XAML MediaElement control.  
  
On Universal Windows Platform, there generally isn't a movie resolution or
bitrate limit, however, higher resolution or bitrate movies consume more
memory for decoding. Weaker devices also start skipping frames much sooner at
extremely high resolutions. To find a list of supported formats for this
platform, refer to the Microsoft documentation on [Supported audio and video
formats (Windows Runtime apps)](https://learn.microsoft.com/en-us/previous-
versions/windows/apps/hh986969\(v=win.10\)?redirectedfrom=MSDN).  
  
**Android:** When an Android phone is in standby mode,
`Handheld.PlayFullScreenMovie` function pauses the movie playback. When the
phone is turned back on, the movie playback resumes over the lock screen if
you're using a developement build. You have the option to switch back to the
standard lock screen display.  
  

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Handheld.PlayFullScreenMovie](Handheld.PlayFullScreenMovie.html)("StarWars.mp4", [Color.black](Color-black.html), [FullScreenMovieControlMode.CancelOnInput](FullScreenMovieControlMode.CancelOnInput.html));
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

