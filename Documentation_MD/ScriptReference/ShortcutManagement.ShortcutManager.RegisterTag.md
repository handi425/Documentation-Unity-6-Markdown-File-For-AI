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

#  [ShortcutManager](ShortcutManagement.ShortcutManager.html).RegisterTag

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

public static void RegisterTag(string tag);

## Declaration

public static void RegisterTag(Enum e);

### Parameters

tag | Context string identifier.  
---|---  
e | Context enum identifier.  
  
### Description

Registers the tag as a custom context used to filter shortcuts after a window
context is determined.

Use this method to define contexts that span across Editor windows, or
encompass certain window states and GUI controls.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.ShortcutManagement;
    using UnityEngine;  
      
    public class MyWindow : [EditorWindow](EditorWindow.html)
    {
        const [KeyCode](KeyCode.html) shortcutKey = [KeyCode.A](KeyCode.A.html);  
      
        public enum MyTool
        {
            EmptyTool,
            ShortcutTool
        }  
      
        MyTool tool;
        MyTool [Tool](Tool.html)
        {
            get => tool;
            set
            {
                if (tool == value) return;  
      
                [ShortcutManager.RegisterTag](ShortcutManagement.ShortcutManager.RegisterTag.html)(tool = value);
                [Debug.Log](Debug.Log.html)($"{tool} tool registered");
            }
        }  
      
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
      
        [Shortcut("Tags/Shortcut [Tool](Tool.html)", typeof(MyWindow), "MyTool.ShortcutTool", shortcutKey)]
        static void ShortcutToolShortcut()
        {
            [Debug.Log](Debug.Log.html)($"Shortcut for MyWindow with 'MyTool.ShortcutTool' tag context executed");
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
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("[Tools](Tools.html)");
            [Tool](Tool.html) = (MyTool)[EditorGUILayout.EnumPopup](EditorGUILayout.EnumPopup.html)("Custom [Tool](Tool.html)", [Tool](Tool.html));
            CustomTag = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Custom Tag", CustomTag);  
      
            [EditorGUILayout.Space](EditorGUILayout.Space.html)();
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)($"The default binding for window shortcuts is {shortcutKey}");
        }
    }
    

When you use these tags, be careful not to leave outdated tags registered.
Doing so can result in multiple available shortcuts, which opens a shortcut
conflict window. Use UnregisterTag to unregister tags.  
  
If you use an enum overload, Unity automatically clears tags from previous
values of that enum.  
  
Unity also provides built-in support for certain enums. For example,
UnityEditor.Tool and UnityEditor.ViewTool.  
  
Additional resources: UnregisterTag.

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

