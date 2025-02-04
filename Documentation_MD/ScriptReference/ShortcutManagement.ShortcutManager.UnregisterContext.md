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

#
[ShortcutManager](ShortcutManagement.ShortcutManager.html).UnregisterContext

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

public static void
UnregisterContext([ShortcutManagement.IShortcutContext](ShortcutManagement.IShortcutContext.html)
context);

### Parameters

context | The custom context to remove from the shortcut context list.  
---|---  
  
### Description

Removes a [IShortcutContext](ShortcutManagement.IShortcutContext.html) from
the shortcut context list.

Additional resources:
[ShortcutManager.RegisterContext](ShortcutManagement.ShortcutManager.RegisterContext.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.ShortcutManagement;
    using UnityEngine;
    
    public class ShortcutContextSample : [EditorWindow](EditorWindow.html)
    {
        public class CustomShortcutContext : [IShortcutContext](ShortcutManagement.IShortcutContext.html)
        {
            public bool active
            {
                get
                {
                    if (!(focusedWindow is ShortcutContextSample view))
                        return false;
    
                    return view.toggleValue;
                }
            }
        }
    
        [Shortcut("Custom Shortcut Context/[Sample](PackageManager.UI.Sample.html) Shortcut", typeof(CustomShortcutContext), [KeyCode.Mouse1](KeyCode.Mouse1.html))]
        static void SampleShortcut([ShortcutArguments](ShortcutManagement.ShortcutArguments.html) args)
        {
            [Debug.Log](Debug.Log.html)("The sample shortcut was called.");
        }
    
        bool m_ToggleValue = false;
        public bool toggleValue => m_ToggleValue;
    
        CustomShortcutContext m_ShortcutContext = new CustomShortcutContext();
    
        [[MenuItem](MenuItem.html)("Window/Custom [Editor](Editor.html) Window")]
        public static void ShowWindow()
        {
            ShortcutContextSample wnd = GetWindow<ShortcutContextSample>();
            wnd.titleContent = new [GUIContent](GUIContent.html)("Custom [Editor](Editor.html) Window");
        }
    
        void OnGUI()
        {
            var content = new [GUIContent](GUIContent.html)("[Toggle](UIElements.Toggle.html)", "[Toggle](UIElements.Toggle.html) to activate the shortcut context.");
            m_ToggleValue = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)(content, m_ToggleValue);
        }
    
        private void OnEnable()
        {
            [ShortcutManager.RegisterContext](ShortcutManagement.ShortcutManager.RegisterContext.html)(m_ShortcutContext);
        }
    
        private void OnDisable()
        {
            [ShortcutManager.UnregisterContext](ShortcutManagement.ShortcutManager.UnregisterContext.html)(m_ShortcutContext);
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

