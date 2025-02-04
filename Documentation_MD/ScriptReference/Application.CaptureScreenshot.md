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

**Removed**  

#  [Application](Application.html).CaptureScreenshot

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

**Obsolete** Application.CaptureScreenshot is obsolete. Use
ScreenCapture.CaptureScreenshot instead.  
**Upgrade to[CaptureScreenshot](ScreenCapture.CaptureScreenshot.html)**

## Declaration

public static void CaptureScreenshot(string filename);

**Obsolete** Application.CaptureScreenshot is obsolete. Use
ScreenCapture.CaptureScreenshot instead.  
**Upgrade to[CaptureScreenshot](ScreenCapture.CaptureScreenshot.html)**

## Declaration

public static void CaptureScreenshot(string filename, int superSize);

### Parameters

filename | Pathname to save the screenshot file to.  
---|---  
superSize | Factor by which to increase resolution.  
  
### Description

Captures a screenshot at path `filename` as a PNG file.

Use [ScreenCapture.CaptureScreenshot](ScreenCapture.CaptureScreenshot.html)
instead of obsolete Application.CaptureScreenshot.  
  
If the image file exists already, it will be overwritten. The location where
the image is written to can include a directory/folder list. For example on
macOS the PNG file could be written to `/tmp/ScreenGrab.png`. With no
directory/folder list the image will be written into the Project folder.
CaptureScreenshot() can also be used from the Editor, for example in a custom
`EditorWindow`. By default the screen grabbed image will also be written into
the Project folder. Also, the Game view must be selected in order for the
Editor screen capture to work.  
  
When `superSize` parameter is larger than 1, a larger resolution screenshot
will be produced. For example, passing 4 will make the screenshot be 4x4
larger than it would normally be. This is useful to produce screenshots for
printing.  
  
On mobile platforms the filename is appended to the persistent data path. See
[Application.persistentDataPath](Application-persistentDataPath.html) for more
information. On Android this function returns immediately. The resulting
screenshot is available later.  
  
**Note:** Screenshots can be made from the Editor as described above. In this
case only the Game view can be captured. If the Scene view is selected any
screenshot will not be written. Switching to the Game view will cause the most
recent captured image to be written. See [EditorWindow](EditorWindow.html) for
how an editor-based capture window can be created. If the Game view is current
and the Editor button is clicked multiple times the first generated screenshot
will be written. `Application.CaptureScreenshot` is a Game specific function.

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

