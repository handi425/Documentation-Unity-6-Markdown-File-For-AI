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

#  [EditorWindow](EditorWindow.html).wantsMouseEnterLeaveWindow

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

public bool wantsMouseEnterLeaveWindow;

### Description

Checks whether MouseEnterWindow and MouseLeaveWindow events are received in
the GUI in this Editor window.

If set to true, the window recieves an OnGUI call whenever the mouse enters or
leaves a window.  
  
**Note:** This function does not trigger Repaint() Automatically. Also,
entering or leaving a window while a mouse button is pressed does not trigger
either event, as pressing the mouse button activates drag mode (see
[EventType.MouseDrag](EventType.MouseDrag.html) and other drag-related events
for more information).

    
    
    // [Editor](Editor.html) Script that shows how mouse enter and leave window events
    // get caught in the [Editor](Editor.html) window
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    
    public class WantsMouseEnterLeaveWindowEx : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/wantsMouseEnterLeaveWindow example")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) editorWindow = GetWindow(typeof(WantsMouseEnterLeaveWindowEx));
            editorWindow.Show();
        }
    
        public void OnGUI()
        {
            wantsMouseEnterLeaveWindow = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Receive Enter/Leave: ", wantsMouseEnterLeaveWindow);
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Check Console for MouseEnter/LeaveWindow messages");
    
            // Repaint the window as wantsMouseEnterLeaveWindow doesn't trigger a repaint automatically
            if (Event.current.type == [EventType.MouseEnterWindow](EventType.MouseEnterWindow.html) ||
                Event.current.type == [EventType.MouseLeaveWindow](EventType.MouseLeaveWindow.html))
            {
                [Debug.Log](Debug.Log.html)("Received event " +
                    ((Event.current.type == [EventType.MouseEnterWindow](EventType.MouseEnterWindow.html)) ? "MouseEnterWindow" : "MouseLeaveWindow"));
                Repaint();
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

