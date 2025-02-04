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

#  [PluginImporter](PluginImporter.html).SetIcon

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

public void SetIcon(string className, [Texture2D](Texture2D.html) icon);

### Parameters

className | The fully qualified class name of a [MonoScript](MonoScript.html) imported by this managed plugin.  
---|---  
icon | The custom icon to associate with the imported [MonoScript](MonoScript.html). When the value is null, Unity restores the default icon.  
  
### Description

Sets the custom icon to associate with a [MonoScript](MonoScript.html)
imported by a managed plugin.

Each [MonoScript](MonoScript.html) imported by managed plugins can have an
associated custom icon. This icon is used in the Scene view, the Inspector,
and the Project window. To remove a [MonoScript](MonoScript.html)'s associated
custom icon, pass null to this method.  
  
Additional resources: [MonoScript.GetClass](MonoScript.GetClass.html),
Type.FullName, [PluginImporter.GetIcon](PluginImporter.GetIcon.html),
[MonoImporter.SetIcon](MonoImporter.SetIcon.html),
[EditorGUIUtility.SetIconForObject](EditorGUIUtility.SetIconForObject.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Example
    {
        [[MenuItem](MenuItem.html)("Examples/Set Custom Icon on Managed [Plugin](VersionControl.Plugin.html) [MonoScript](MonoScript.html)")]
        static void SetCustomIconOnManagedPluginMonoScript()
        {
            var dllPath = "Assets/MyManagedPlugin.dll";
            var iconPath = "Assets/MyIcon.png";
            var pluginImporter = [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)(dllPath) as [PluginImporter](PluginImporter.html);
            var monoScript = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[MonoScript](MonoScript.html)>(dllPath);
            var icon = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture2D](Texture2D.html)>(iconPath);  
      
            pluginImporter.SetIcon(monoScript.GetClass().FullName, icon);
            pluginImporter.SaveAndReimport();
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

