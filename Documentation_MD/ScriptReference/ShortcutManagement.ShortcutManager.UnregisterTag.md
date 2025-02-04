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

#  [ShortcutManager](ShortcutManagement.ShortcutManager.html).UnregisterTag

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

public static void UnregisterTag(string tag);

### Parameters

tag | Context string identifier.  
---|---  
  
### Description

Removes a tag from the custom context list.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.ShortcutManagement;
    using UnityEngine;  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        const [KeyCode](KeyCode.html) shortcutKey = [KeyCode.A](KeyCode.A.html);  
      
        bool customTag;
        bool CustomTag
        {
            get => customTag;
            set
            {
                if (customTag == value) return;  
      
                customTag = value;
                var tag = nameof(customTag);  
      
                if (customTag)
                {
                    [ShortcutManager.RegisterTag](ShortcutManagement.ShortcutManager.RegisterTag.html)(tag);
                    [Debug.Log](Debug.Log.html)($"{tag} enabled");
                }
                else
                {
                    [ShortcutManager.UnregisterTag](ShortcutManagement.ShortcutManager.UnregisterTag.html)(tag);
                    [Debug.Log](Debug.Log.html)($"{tag} disabled");
                }
            }
        }  
      
        [Shortcut("Tags/No Tag", typeof(MyWindow), shortcutKey)]
        static void NoTagShortcut()
        {
            [Debug.Log](Debug.Log.html)($"Shortcut for MyWindow without tag context executed");
        }  
      
        [Shortcut("Tags/Custom Tag", typeof(MyWindow), nameof(customTag), shortcutKey)]
        static void CustomTagShortcut()
        {
            [Debug.Log](Debug.Log.html)($"Shortcut for MyWindow with {nameof(customTag)} tag context executed");
        }  
      
        [[MenuItem](MenuItem.html)("Window/My Window")]
        static void OpenWindow() => [EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(MyWindow)).Show();  
      
        void OnGUI()
        {
            CustomTag = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Custom Tag", CustomTag);  
      
            [EditorGUILayout.Space](EditorGUILayout.Space.html)();
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)($"The default binding for window shortcuts is {shortcutKey}");
        }
    }
    

Additional resources: RegisterTag.

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

