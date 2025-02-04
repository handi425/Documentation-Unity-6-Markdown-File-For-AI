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

#  [GUI](GUI.html).Box

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

public static void Box([Rect](Rect.html) position, string text);

## Declaration

public static void Box([Rect](Rect.html) position, [Texture](Texture.html)
image);

## Declaration

public static void Box([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content);

## Declaration

public static void Box([Rect](Rect.html) position, string text,
[GUIStyle](GUIStyle.html) style);

## Declaration

public static void Box([Rect](Rect.html) position, [Texture](Texture.html)
image, [GUIStyle](GUIStyle.html) style);

## Declaration

public static void Box([Rect](Rect.html) position,
[GUIContent](GUIContent.html) content, [GUIStyle](GUIStyle.html) style);

### Parameters

position | Rectangle on the screen to use for the box.  
---|---  
text | Text to display on the box.  
image |  [Texture](Texture.html) to display on the box.  
content | Text, image and tooltip for this box.  
style | The style to use. If left out, the `box` style from the current [GUISkin](GUISkin.html) is used.  
  
### Description

Create a Box on the GUI Layer.

A Box can contain text, an image, or a combination of these along with an
optional tooltip, through using a [GUIContent](GUIContent.html) parameter. You
may also use a [GUIStyle](GUIStyle.html) to adjust the layout of items in a
box, text colour and other properties.  
  
Here is an example of a Box containing Text:

    
    
    using UnityEngine;  
      
    public class BoxExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)), "This is a box");
        }
    }
    

Here is an example of a Box containing a Texture:

    
    
    using UnityEngine;  
      
    public class BoxWithTextureExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture](Texture.html) BoxTexture;      // Drag a [Texture](Texture.html) onto this item in the Inspector  
      
        void OnGUI()
        {
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)), BoxTexture);
        }
    }
    

Here is an example of a Box containing a GUIContent, combining Text, Texture
and Tooltip:

    
    
    using UnityEngine;  
      
    public class BoxWithContentExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture](Texture.html) BoxTexture;      // Drag a [Texture](Texture.html) onto this item in the Inspector  
      
        [GUIContent](GUIContent.html) content;  
      
        void Start()
        {
            content = new [GUIContent](GUIContent.html)("This is a box", BoxTexture, "This is a tooltip");
        }  
      
        void OnGUI()
        {
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)), content);
        }
    }
    

Here is an example of a Box containing Text, with options set in a GUIStyle to
position the Text in the center of the Box.

    
    
    using UnityEngine;  
      
    public class BoxWithTextStyleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [GUIStyle](GUIStyle.html) style = new [GUIStyle](GUIStyle.html)();  
      
        void Start()
        {
            // [Position](UIElements.Position.html) the Text in the center of the [Box](UIElements.Box.html)
            style.alignment = [TextAnchor.MiddleCenter](TextAnchor.MiddleCenter.html);
        }  
      
        void OnGUI()
        {
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)), "This is a box", style);
        }
    }
    

Here is an example of a Box containing a Texture, with options set in a
GUIStyle to position the Texture in the center of the Box.

    
    
    using UnityEngine;  
      
    public class BoxWithTextureStyleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture](Texture.html) BoxTexture;              // Drag a [Texture](Texture.html) onto this item in the Inspector  
      
        [GUIStyle](GUIStyle.html) style = new [GUIStyle](GUIStyle.html)();  
      
    
        void Start()
        {
            // [Position](UIElements.Position.html) the [Texture](Texture.html) in the center of the [Box](UIElements.Box.html)
            style.alignment = [TextAnchor.MiddleCenter](TextAnchor.MiddleCenter.html);
        }  
      
        void OnGUI()
        {
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)), BoxTexture, style);
        }
    }
    

Finally, here is an example of a Box containing a GUIContent, combining Text,
Texture and Tooltip, with positional information contained in the GUIStyle
parameter:

    
    
    using UnityEngine;  
      
    public class BoxWithContentStyleExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture](Texture.html) BoxTexture;              // Drag a [Texture](Texture.html) onto this item in the Inspector  
      
        [GUIContent](GUIContent.html) content;
        [GUIStyle](GUIStyle.html) style = new [GUIStyle](GUIStyle.html)();  
      
        void Start()
        {
            content = new [GUIContent](GUIContent.html)("This is a box", BoxTexture, "This is a tooltip");  
      
            // [Position](UIElements.Position.html) the Text and [Texture](Texture.html) in the center of the box
            style.alignment = [TextAnchor.MiddleCenter](TextAnchor.MiddleCenter.html);  
      
            // [Position](UIElements.Position.html) the Text below the [Texture](Texture.html) (rather than to the right of it)
            style.imagePosition = [ImagePosition.ImageAbove](ImagePosition.ImageAbove.html);
        }  
      
        void OnGUI()
        {
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(0, 0, [Screen.width](Screen-width.html), [Screen.height](Screen-height.html)), content, style);
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

