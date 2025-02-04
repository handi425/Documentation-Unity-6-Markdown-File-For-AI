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

#  [GUILayout](GUILayout.html).Window

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

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) screenRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, string text, params
GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) screenRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, [Texture](Texture.html)
image, params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) screenRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func,
[GUIContent](GUIContent.html) content, params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) screenRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, string text,
[GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) screenRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, [Texture](Texture.html)
image, [GUIStyle](GUIStyle.html) style, params GUILayoutOption[] options);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) screenRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style, params
GUILayoutOption[] options);

### Parameters

id | A unique ID to use for each window. This is the ID you'll use to interface to it.  
---|---  
screenRect | Rectangle on the screen to use for the window. The layouting system will attempt to fit the window inside it - if that cannot be done, it will adjust the rectangle to fit.  
func | The function that creates the GUI `inside` the window. This function must take one parameter - the `id` of the window it's currently making GUI for.  
text | Text to display as a title for the window.  
image |  [Texture](Texture.html) to display an image in the titlebar.  
content | Text, image and tooltip for this window.  
style | An optional style to use for the window. If left out, the `window` style from the current [GUISkin](GUISkin.html) is used.  
options | An optional list of layout options that specify extra layouting properties. Any values passed in here will override settings defined by the `style` or the `screenRect` you pass in.  
Additional resources: [GUILayout.Width](GUILayout.Width.html),
[GUILayout.Height](GUILayout.Height.html),
[GUILayout.MinWidth](GUILayout.MinWidth.html),
[GUILayout.MaxWidth](GUILayout.MaxWidth.html),
[GUILayout.MinHeight](GUILayout.MinHeight.html),
[GUILayout.MaxHeight](GUILayout.MaxHeight.html),
[GUILayout.ExpandWidth](GUILayout.ExpandWidth.html),
[GUILayout.ExpandHeight](GUILayout.ExpandHeight.html).  
  
### Returns

**Rect** The rectangle the window is at. This can be in a different position
and have a different size than the one you passed in.

### Description

Make a popup window that layouts its contents automatically.

Windows float above normal GUI controls, feature click-to-focus and can
optionally be dragged around by the end user. Unlike other controls, you need
to pass them a separate function for the GUI controls to put inside the
window. Here is a small example to get you started:  
  
![](../StaticFiles/ScriptRefImages/GUILayoutWindow.png)  
_Window in the Game View._

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rect](Rect.html) windowRect = new [Rect](Rect.html)(20, 20, 120, 50);  
      
        void OnGUI()
        {
            // Register the window. Notice the 3rd parameter
            windowRect = [GUILayout.Window](GUILayout.Window.html)(0, windowRect, DoMyWindow, "My Window");
        }  
      
        // Make the contents of the window
        void DoMyWindow(int windowID)
        {
            // This button will size to fit the window
            if ([GUILayout.Button](GUILayout.Button.html)("Hello World"))
            {
                print("Got a click");
            }
        }
    }
    

The screen rectangle you pass in to the function only acts as a guide. To
Apply extra limits to the window, pass in some extra layout options. The ones
applied here will override the size calculated. Here is a small example:

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rect](Rect.html) windowRect = new [Rect](Rect.html)(20, 20, 120, 50);  
      
        void OnGUI()
        {
            // Register the window. Here we instruct the layout system to
            // make the window 100 pixels wide no matter what.
            windowRect = [GUILayout.Window](GUILayout.Window.html)(0, windowRect, DoMyWindow, "My Window", [GUILayout.Width](GUILayout.Width.html)(100));
        }  
      
        // Make the contents of the window
        void DoMyWindow(int windowID)
        {
            // This button is too large to fit the window
            // Normally, the window would have been expanded to fit the button, but due to
            // the [GUILayout.Width](GUILayout.Width.html) call above the window will only ever be 100 pixels wide
            if ([GUILayout.Button](GUILayout.Button.html)("Please click me a lot"))
            {
                print("Got a click");
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

