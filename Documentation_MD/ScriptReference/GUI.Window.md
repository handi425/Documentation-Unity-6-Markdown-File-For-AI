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

#  [GUI](GUI.html).Window

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

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) clientRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, string text);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) clientRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, [Texture](Texture.html)
image);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) clientRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func,
[GUIContent](GUIContent.html) content);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) clientRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) clientRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func, [Texture](Texture.html)
image, [GUIStyle](GUIStyle.html) style);

## Declaration

public static [Rect](Rect.html) Window(int id, [Rect](Rect.html) clientRect,
[GUI.WindowFunction](GUI.WindowFunction.html) func,
[GUIContent](GUIContent.html) title, [GUIStyle](GUIStyle.html) style);

### Parameters

Style | An optional style to use for the window. If left out, the `window` style from the current [GUISkin](GUISkin.html) is used.  
---|---  
id | ID number for the window (can be any value as long as it is unique).  
clientRect | Onscreen rectangle denoting the window's position and size.  
func | Script function to display the window's contents.  
text | Text to render inside the window.  
image | Image to render inside the window.  
content | GUIContent to render inside the window.  
style | Style information for the window.  
title | Text displayed in the window's title bar.  
  
### Returns

**Rect** Onscreen rectangle denoting the window's position and size.

### Description

Make a popup window.

Windows float above normal GUI controls, feature click-to-focus and can
optionally be dragged around by the end user. Unlike other controls, you need
to pass them a separate function that renders the GUI controls inside the
window.  
  
**Note:** If you are using [GUILayout](GUILayout.html) to place your
components inside the window, you should use
[GUILayout.Window](GUILayout.Window.html). Also, if
[MonoBehaviour.useGUILayout](MonoBehaviour-useGUILayout.html) is set to false
then a call to GUI.Window will not have any effect, even though it is not a
GUILayout function.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rect](Rect.html) windowRect = new [Rect](Rect.html)(20, 20, 120, 50);  
      
        void OnGUI()
        {
            // Register the window. Notice the 3rd parameter
            windowRect = [GUI.Window](GUI.Window.html)(0, windowRect, DoMyWindow, "My Window");
        }  
      
        // Make the contents of the window
        void DoMyWindow(int windowID)
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 20, 100, 20), "Hello World"))
            {
                print("Got a click");
            }
        }
    }
    

You can use the same function to create multiple windows. Just make sure that
_each window has its own ID_. Example:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rect](Rect.html) windowRect0 = new [Rect](Rect.html)(20, 20, 120, 50);
        public [Rect](Rect.html) windowRect1 = new [Rect](Rect.html)(20, 100, 120, 50);  
      
        void OnGUI()
        {
            // Register the window. We create two windows that use the same function
            // Notice that their IDs differ
            windowRect0 = [GUI.Window](GUI.Window.html)(0, windowRect0, DoMyWindow, "My Window");
            windowRect1 = [GUI.Window](GUI.Window.html)(1, windowRect1, DoMyWindow, "My Window");
        }  
      
        // Make the contents of the window
        void DoMyWindow(int windowID)
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 20, 100, 20), "Hello World"))
            {
                print("Got a click in window " + windowID);
            }  
      
            // Make the windows be draggable.
            [GUI.DragWindow](GUI.DragWindow.html)(new [Rect](Rect.html)(0, 0, 10000, 10000));
        }
    }
    

To stop showing a window, simply stop calling GUI.Window from inside your main
OnGUI function:

    
    
    // boolean variable to decide whether to show the window or not.
    // Change this from the in-game [GUI](GUI.html), scripting, the inspector or anywhere else to
    // decide whether the window is visible  
      
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public bool doWindow0 = true;  
      
        // Make the contents of the window.
        void DoWindow0(int windowID)
        {
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 30, 80, 20), "Click Me!");
        }  
      
        void OnGUI()
        {
            // Make a toggle button for hiding and showing the window
            doWindow0 = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(10, 10, 100, 20), doWindow0, "Window 0");  
      
            // Make sure we only call [GUI.Window](GUI.Window.html) if doWindow0 is true.
            if (doWindow0)
            {
                [GUI.Window](GUI.Window.html)(0, new [Rect](Rect.html)(110, 10, 200, 60), DoWindow0, "Basic Window");
            }
        }
    }
    

To make a window that gets its size from automatic GUI layouting, use
[GUILayout.Window](GUILayout.Window.html). **Call Ordering** Windows need to
be drawn back-to-front; windows on top of other windows need to be drawn later
than the ones below them. This means that you can not count on your DoWindow
functions to be called in any particular order. In order for this to work
seamlessly, the following values are stored when you create your window (using
the **Window** function), and retrieved when your DoWindow gets called:
[GUI.skin](GUI-skin.html), [GUI.enabled](GUI-enabled.html), [GUI.color](GUI-
color.html), [GUI.backgroundColor](GUI-backgroundColor.html),
[GUI.contentColor](GUI-contentColor.html), [GUI.matrix](GUI-matrix.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Rect](Rect.html) windowRect0 = new [Rect](Rect.html)(20, 20, 120, 50);
        public [Rect](Rect.html) windowRect1 = new [Rect](Rect.html)(20, 100, 120, 50);  
      
        void OnGUI()
        {
            // Here we make 2 windows. We set the [GUI.color](GUI-color.html) value to something before each.
            [GUI.color](GUI-color.html) = [Color.red](Color-red.html);
            windowRect0 = [GUI.Window](GUI.Window.html)(0, windowRect0, DoMyWindow, "Red Window");  
      
            [GUI.color](GUI-color.html) = [Color.green](Color-green.html);
            windowRect1 = [GUI.Window](GUI.Window.html)(1, windowRect1, DoMyWindow, "Green Window");
        }  
      
        // Make the contents of the window.
        // The value of [GUI.color](GUI-color.html) is set to what it was when the window
        // was created in the code above.
        void DoMyWindow(int windowID)
        {
            if ([GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 20, 100, 20), "Hello World"))
            {
                print("Got a click in window with color " + [GUI.color](GUI-color.html));
            }  
      
            // Make the windows be draggable.
            [GUI.DragWindow](GUI.DragWindow.html)(new [Rect](Rect.html)(0, 0, 10000, 10000));
        }
    }
    

Note that you can use the alpha component of [GUI.color](GUI-color.html) to
fade windows in and out.  
  
Additional resources: [DragWindow](GUI.DragWindow.html),
[BringWindowToFront](GUI.BringWindowToFront.html),
[BringWindowToBack](GUI.BringWindowToBack.html).

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

