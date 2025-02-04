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

#  [EditorGUIUtility](EditorGUIUtility.html).SetIconForObject

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

public static void SetIconForObject([Object](Object.html) obj,
[Texture2D](Texture2D.html) icon);

### Parameters

obj | The [GameObject](GameObject.html) or [MonoScript](MonoScript.html) to associate the icon with.  
---|---  
icon | The custom icon to associate with the [GameObject](GameObject.html) or [MonoScript](MonoScript.html). When this value is null, the default icon is restored.  
  
### Description

Sets a custom icon to associate with a [GameObject](GameObject.html) or
[MonoScript](MonoScript.html). The custom icon is displayed in the Scene view
and the Inspector.

Custom icons for GameObjects are saved in the scene.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class Example
    {
        [[MenuItem](MenuItem.html)("Examples/Set Custom Icon on [GameObject](GameObject.html)")]
        public static void SetCustomIconOnGameObject()
        {
            var go = new [GameObject](GameObject.html)();
            var icon = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture2D](Texture2D.html)>("Assets/MyIcon.png");  
      
            [EditorGUIUtility.SetIconForObject](EditorGUIUtility.SetIconForObject.html)(go, icon);
        }
    }
    

Using this function, you can set custom icons directly on a
[MonoScript](MonoScript.html). However the next time the script is reimported,
the change will be lost.  
  
To make the custom icon persistent, call
[MonoImporter.SetIcon](MonoImporter.SetIcon.html) and
[AssetImporter.SaveAndReimport](AssetImporter.SaveAndReimport.html). If the
script is in a managed plugin, call
[PluginImporter.SetIcon](PluginImporter.SetIcon.html) instead of
[MonoImporter.SetIcon](MonoImporter.SetIcon.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    class Example
    {
        [[MenuItem](MenuItem.html)("Examples/Set Custom Icon on [MonoScript](MonoScript.html)")]
        public static void SetCustomIconOnMonoScript()
        {
            var monoImporter = [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)("Assets/MyMonoBehaviour.cs") as [MonoImporter](MonoImporter.html);
            var monoScript = monoImporter.GetScript();
            var icon = [AssetDatabase.LoadAssetAtPath](AssetDatabase.LoadAssetAtPath.html)<[Texture2D](Texture2D.html)>("Assets/MyIcon.png");  
      
            [EditorGUIUtility.SetIconForObject](EditorGUIUtility.SetIconForObject.html)(monoScript, icon);  
      
            // make the custom icon persistent
            monoImporter.SetIcon(icon);
            monoImporter.SaveAndReimport();
        }
    }
    

When you set custom icons from a GUI, it is recommended that you defer
reimport until the GUI is closed. If you reimport before the GUI is closed,
the domain reload caused by recompiling the script could lead to a poor user
experience.  
  
Additional resources: [MonoImporter](MonoImporter.html),
[PluginImporter](PluginImporter.html).

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

