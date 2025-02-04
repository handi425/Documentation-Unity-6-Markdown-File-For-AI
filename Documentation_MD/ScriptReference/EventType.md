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

# EventType

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

Types of UnityGUI input and processing events.

Use this to tell which type of event has taken place in the GUI. Types of
Events include mouse clicking, mouse dragging, button pressing, the mouse
entering or exiting the window, and the scroll wheel as well as others
mentioned below.  
  
Events can be used to prevent other GUI elements from responding to that
event. Refer to [Event.Use](Event.Use.html).  
  
Additional resources: [Event.type](Event-type.html), [Event](Event.html), [GUI
Scripting Guide](../Manual/GUIScriptingGuide.html).

    
    
    //Attach this script to a [GameObject](GameObject.html)
    //This script is a basic overview of some of the [Event](Event.html) Types available. It outputs messages depending on the current [Event](Event.html) Type.  
      
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [Event](Event.html) m_Event = [Event.current](Event-current.html);  
      
            if (m_Event.type == [EventType.MouseDown](EventType.MouseDown.html))
            {
                [Debug.Log](Debug.Log.html)("Mouse Down.");
            }  
      
            if (m_Event.type == [EventType.MouseDrag](EventType.MouseDrag.html))
            {
                [Debug.Log](Debug.Log.html)("Mouse Dragged.");
            }  
      
            if (m_Event.type == [EventType.MouseUp](EventType.MouseUp.html))
            {
                [Debug.Log](Debug.Log.html)("Mouse Up.");
            }
        }
    }
    
    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnGUI()
        {
            [Event](Event.html) m_Event = [Event.current](Event-current.html);  
      
            if (m_Event.type == [EventType.MouseDown](EventType.MouseDown.html))
            {
                if (m_Event.pointerType == [PointerType.Pen](PointerType.Pen.html))     //Check if it's a pen event.
                    [Debug.Log](Debug.Log.html)("Pen Down.");
                else 
                    [Debug.Log](Debug.Log.html)("Mouse Down.");                   //If it's not a pen event, it's a mouse event. 
            }
        }
    }
    

### Properties

[MouseDown](EventType.MouseDown.html)| Mouse button was pressed.  
---|---  
[MouseUp](EventType.MouseUp.html)| Mouse button was released.  
[MouseMove](EventType.MouseMove.html)| Mouse was moved (Editor views only).  
[MouseDrag](EventType.MouseDrag.html)| Mouse was dragged.  
[KeyDown](EventType.KeyDown.html)| A keyboard key was pressed.  
[KeyUp](EventType.KeyUp.html)| A keyboard key was released.  
[ScrollWheel](EventType.ScrollWheel.html)| The scroll wheel was moved.  
[Repaint](EventType.Repaint.html)| A repaint event. One is sent every frame.  
[Layout](EventType.Layout.html)| A layout event.  
[DragUpdated](EventType.DragUpdated.html)| Editor only: drag & drop operation
updated.  
[DragPerform](EventType.DragPerform.html)| Editor only: drag & drop operation
performed.  
[DragExited](EventType.DragExited.html)| Editor only: drag & drop operation
exited.  
[Ignore](EventType.Ignore.html)|  Event should be ignored.  
[Used](EventType.Used.html)| Already processed event.  
[ValidateCommand](EventType.ValidateCommand.html)| Validates a special command
(e.g. copy & paste).  
[ExecuteCommand](EventType.ExecuteCommand.html)| Execute a special command
(eg. copy & paste).  
[ContextClick](EventType.ContextClick.html)| User has right-clicked (or
control-clicked on the mac).  
[MouseEnterWindow](EventType.MouseEnterWindow.html)| Mouse entered a window
(Editor views only).  
[MouseLeaveWindow](EventType.MouseLeaveWindow.html)| Mouse left a window
(Editor views only).  
[TouchDown](EventType.TouchDown.html)| Direct manipulation device (finger,
pen) touched the screen.  
[TouchUp](EventType.TouchUp.html)| Direct manipulation device (finger, pen)
left the screen.  
[TouchMove](EventType.TouchMove.html)| Direct manipulation device (finger,
pen) moved on the screen (drag).  
[TouchEnter](EventType.TouchEnter.html)| Direct manipulation device (finger,
pen) moving into the window (drag).  
[TouchLeave](EventType.TouchLeave.html)| Direct manipulation device (finger,
pen) moved out of the window (drag).  
[TouchStationary](EventType.TouchStationary.html)| Direct manipulation device
(finger, pen) stationary event (long touch down).  
  
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

