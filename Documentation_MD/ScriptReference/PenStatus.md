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

# PenStatus

enumeration

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

Options for specifying the state of the pen. For example, whether the pen is
in contact with the screen or tablet, whether the pen is inverted, and whether
buttons are pressed. You can combine states using bitwise OR operators.

Before you process an event as a pen event, you should check the
[PointerType](PointerType.html) of a mouse event (e.g.
[EventType.MouseDown](EventType.MouseDown.html)).  
  
When a user uses a pen, some mouse events are often mixed with pen events in
the event stream, and you can't distinguish them by type because mouse and pen
events share the same [EventType](EventType.html). Instead, use
[PointerType](PointerType.html) to distinguish them. Otherwise, Unity
processes all incoming mouse events as pen events, which can lead to
unexpected behavior because the mouse events (pointerType = Mouse) do not have
pen event fields, like [PenStatus](PenStatus.html), set.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [Event](Event.html) m_Event = [Event.current](Event-current.html);  
      
            if (m_Event.type == [EventType.MouseDown](EventType.MouseDown.html))
            {
                if (m_Event.pointerType == [PointerType.Pen](PointerType.Pen.html))     //Check if it's a pen event.
                {
                    if (m_Event.penStatus == [PenStatus.None](PenStatus.None.html))
                        [Debug.Log](Debug.Log.html)("Pen is in a neutral state.");
                    else if (m_Event.penStatus == [PenStatus.Inverted](PenStatus.Inverted.html))
                        [Debug.Log](Debug.Log.html)("The pen is inverted.");
                    else if (m_Event.penStatus == [PenStatus.Barrel](PenStatus.Barrel.html))
                        [Debug.Log](Debug.Log.html)("Barrel button on pen is down.");
                    else if (m_Event.penStatus == [PenStatus.Contact](PenStatus.Contact.html))
                        [Debug.Log](Debug.Log.html)("Pen is in contact with screen or tablet.");
                    else if (m_Event.penStatus == [PenStatus.Eraser](PenStatus.Eraser.html))
                        [Debug.Log](Debug.Log.html)("Pen is in erase mode.");
                }
            else
                [Debug.Log](Debug.Log.html)("Mouse Down.");                   //If it's not a pen event, it's a mouse event. 
            }
        }
    }
    

### Properties

[None](PenStatus.None.html)| The pen is in a neutral state.  
---|---  
[Contact](PenStatus.Contact.html)| The pen is in contact with the screen or
tablet.  
[Barrel](PenStatus.Barrel.html)| The barrel button on the pen is currently
pressed.  
[Inverted](PenStatus.Inverted.html)| The pen is inverted.  
[Eraser](PenStatus.Eraser.html)| The pen is in erase mode.  
  
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

