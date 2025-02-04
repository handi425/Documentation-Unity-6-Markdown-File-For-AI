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
[AssetImportContext](AssetImporters.AssetImportContext.html).DependsOnCustomDependency

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

public void DependsOnCustomDependency(string dependency);

### Parameters

dependency | Name of dependency. You can use any name you like, but because these names are global across all your Assets, it can be useful to use a naming convention (eg a path-based naming system as in the example below) to avoid clashes with other custom dependency names.  
---|---  
  
### Description

Allows you to specify that an Asset has a custom dependency.

Use custom dependency if need to setup a dependency to something that can't be
expressed as either an source asset dependency or artifact dependency.

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;
    using UnityEditor.Experimental;
    using UnityEngine.Assertions;
    using [UnityEditor](UnityEditor.html);  
      
    class MySystem
    {
        public const string CustomDependencyName = "MyProject/[Settings](CameraEditor.Settings.html)";  
      
        public static string GetSetting()
        {
            return "42";
        }  
      
        public static void RegisterCustomDependency()
        {
            // You cannot register a custom dependency during the [Asset](VersionControl.Asset.html) Import process, so this method must be called before the [Asset](VersionControl.Asset.html) is imported.
            UnityEditor.AssetDatabase.RegisterCustomDependency(CustomDependencyName, [Hash128.Compute](Hash128.Compute.html)(GetSetting()));
        }
    }  
      
    class SomeValue : [ScriptableObject](ScriptableObject.html)
    {
        public int value;
    }  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "data", AllowCaching = true)]
    public class MyDataImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            ctx.DependsOnCustomDependency(MySystem.CustomDependencyName);  
      
            var someObj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<SomeValue>();  
      
            var setting = MySystem.GetSetting();
            if (setting == "42")
                someObj.value = 100;
            else
                someObj.value = -1;  
      
            ctx.AddObjectToAsset("someObj", someObj);
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

