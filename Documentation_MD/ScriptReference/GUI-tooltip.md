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

#  [GUI](GUI.html).tooltip

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

public static string tooltip;

### Description

The tooltip of the control the mouse is currently over, or which has keyboard
focus. (Read Only).

When you create GUI controls, you can pass in a tooltip for them. This is done
by changing the content parameter to take a custom-made
[GUIContent](GUIContent.html) object, rather than just passing in a string to
display.  
  
When the mouse is over a control with a tooltip, it sets the global
[GUI.tooltip](GUI-tooltip.html) value to the tooltip you pass in. If the mouse
is not hovering over any control, the value is set to the control which has
keyboard focus. At the end of the OnGUI code, you can make a label showing the
value of [GUI.tooltip](GUI-tooltip.html)  
  
![](../StaticFiles/ScriptRefImages/GUITooltip.png)  
_GUI Tooltip on the Game view appears when the mouse is over the button._

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            // Make a button using a custom [GUIContent](GUIContent.html) parameter to pass in the tooltip.
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 10, 100, 20), new [GUIContent](GUIContent.html)("Click me", "This is the tooltip"));  
      
            // [Display](Display.html) the tooltip from the element that has mouseover or keyboard focus
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 40, 100, 40), [GUI.tooltip](GUI-tooltip.html));
        }
    }
    

You can use the ordering of elements to create 'hierarchical' tooltips:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            // This box is larger than many elements following it, and it has a tooltip.
            [GUI.Box](GUI.Box.html)(new [Rect](Rect.html)(5, 35, 110, 75), new [GUIContent](GUIContent.html)("[Box](UIElements.Box.html)", "this box has a tooltip"));  
      
            // This button is inside the box, but has no tooltip so it does not
            // override the box's tooltip.
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 55, 100, 20), "No tooltip here");  
      
            // This button is inside the box, and HAS a tooltip so it overrides
            // the tooltip from the box.
            [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(10, 80, 100, 20), new [GUIContent](GUIContent.html)("I have a tooltip", "The button overrides the box"));  
      
            // finally, display the tooltip from the element that has
            // mouseover or keyboard focus
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(10, 40, 100, 40), [GUI.tooltip](GUI-tooltip.html));
        }
    }
    

Tooltips can also be used to implement an OnMouseOver / OnMouseOut messaging
system:

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public string lastTooltip = " ";  
      
        void OnGUI()
        {
            [GUILayout.Button](GUILayout.Button.html)(new [GUIContent](GUIContent.html)("Play Game", "Button1"));
            [GUILayout.Button](GUILayout.Button.html)(new [GUIContent](GUIContent.html)("Quit", "Button2"));  
      
            if (Event.current.type == [EventType.Repaint](EventType.Repaint.html) && [GUI.tooltip](GUI-tooltip.html) != lastTooltip)
            {
                if (lastTooltip != "")
                {
                    SendMessage(lastTooltip + "OnMouseOut", [SendMessageOptions.DontRequireReceiver](SendMessageOptions.DontRequireReceiver.html));
                }  
      
                if ([GUI.tooltip](GUI-tooltip.html) != "")
                {
                    SendMessage([GUI.tooltip](GUI-tooltip.html) + "OnMouseOver", [SendMessageOptions.DontRequireReceiver](SendMessageOptions.DontRequireReceiver.html));
                }  
      
                lastTooltip = [GUI.tooltip](GUI-tooltip.html);
            }
        }  
      
        void Button1OnMouseOver()
        {
            [Debug.Log](Debug.Log.html)("Play game got focus");
        }  
      
        void Button2OnMouseOut()
        {
            [Debug.Log](Debug.Log.html)("Quit lost focus");
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

