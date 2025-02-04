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

#  [Event](Event.html).Use

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

public void Use();

### Description

Use this event.

Call this method when you've used an event. The event's type will be set to
[EventType.Used](EventType.Used.html), causing other GUI elements to ignore
it.  
  
Events of type [EventType.Repaint](EventType.Repaint.html) and
[EventType.Layout](EventType.Layout.html) should not be used. Attempting to
call this method on such events will issue a warning.  
  
The following example demonstrates how events are consumed and used up. Copy
this code into a script, and open the Example Window this sample creates from
the Window menu.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class ExampleWindow : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Window/Show Example Window")]
        public static void ShowWindow()
        {
            GetWindow(typeof(ExampleWindow));
        }  
      
        private void OnGUI()
        {
            if (Event.current.type == [EventType.MouseDown](EventType.MouseDown.html) && Event.current.button == 0)
            {
                [Debug.Log](Debug.Log.html)("Left clicked at: " + Event.current.mousePosition);
                // This if statement Uses up the current MouseDown event so that
                // subsequent code or [GUI](GUI.html) elements ignore this MouseDown event. 
                Event.current.Use();
            }  
      
            // This if statement does not check Event.current.button, but it only triggers
            // when Event.current.button is not 0 because the previous if statement will
            // Use up the MouseDown event if it is. 
            if (Event.current.type == [EventType.MouseDown](EventType.MouseDown.html)) 
            {
                [Debug.Log](Debug.Log.html)("This only prints when we right click!");
                Event.current.Use();
            }
        }
    }

The following example demonstrates how handles such as
[Handles.PositionHandle](Handles.PositionHandle.html) and
[Handles.FreeMoveHandle](Handles.FreeMoveHandle.html) might use events.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public static class CustomHandle
    {
        public static bool DoHandle([Vector3](Vector3.html) worldpos, float size, float pickSize)
        {
            int id = [GUIUtility.GetControlID](GUIUtility.GetControlID.html)([FocusType.Passive](FocusType.Passive.html));
            [Event](Event.html) evt = [Event.current](Event-current.html);  
      
            bool clicked = false;  
      
            switch (evt.GetTypeForControl(id))
            {
                case [EventType.MouseDown](EventType.MouseDown.html):
                    if (evt.button == 0 && [HandleUtility.nearestControl](HandleUtility-nearestControl.html) == id)
                    {
                        [GUIUtility.hotControl](GUIUtility-hotControl.html) = id;  
      
                        evt.Use(); // Using the MouseDown event
                        clicked = true;
                    }
                    break;  
      
                case [EventType.MouseMove](EventType.MouseMove.html):
                    [HandleUtility.Repaint](HandleUtility.Repaint.html)(); 
                    evt.Use(); // Using the MouseMove event
                    break;  
      
                case [EventType.MouseUp](EventType.MouseUp.html):
                    if (evt.button == 0 && [HandleUtility.nearestControl](HandleUtility-nearestControl.html) == id)
                    {
                        [GUIUtility.hotControl](GUIUtility-hotControl.html) = 0;
                        evt.Use(); // Using the MouseUp event
                    }
                    break;  
      
                case [EventType.Layout](EventType.Layout.html):
                    [HandleUtility.AddControl](HandleUtility.AddControl.html)(id, [HandleUtility.DistanceToCircle](HandleUtility.DistanceToCircle.html)(worldpos, pickSize));
                    // Keep in mind [Layout](Overlays.Layout.html) events should not be Used!
                    break;  
      
                case [EventType.Repaint](EventType.Repaint.html):
                    // Draw the handle here
                    // Keep in mind Repaint events should not be Used!
                    break;
            }  
      
            return clicked;
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

