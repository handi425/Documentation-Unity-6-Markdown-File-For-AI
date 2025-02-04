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

# AssignType

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

An assign type for property elements.

Properties in gradle files use different ways to assign a value. Use the
`AssignType` parameter to choose which way to assign the property value.

    
    
    using [Unity.Android.Gradle](Unity.Android.Gradle.html);
    using UnityEditor.Android;  
      
    public class ModifyProject : [AndroidProjectFilesModifier](Android.AndroidProjectFilesModifier.html)
    {
        public override void OnModifyAndroidProjectFiles([AndroidProjectFiles](Android.AndroidProjectFiles.html) projectFiles)
        {
            // This will produce "buildToolsVersion = '30.0.0'"
            projectFiles.UnityLibraryBuildGradle.Android.BuildToolsVersion.Set("30.0.0", [AssignType.Equals](Unity.Android.Gradle.AssignType.Equals.html));
            // This will produce "compileSdk(30)"
            projectFiles.UnityLibraryBuildGradle.Android.CompileSdk.Set(30, [AssignType.Parentheses](Unity.Android.Gradle.AssignType.Parentheses.html));
        }
    }
    

### Properties

[None](Unity.Android.Gradle.AssignType.None.html)| Places value after a space:
property value.  
---|---  
[Equals](Unity.Android.Gradle.AssignType.Equals.html)| Places value after an
equals: property = value.  
[PlusEquals](Unity.Android.Gradle.AssignType.PlusEquals.html)| Places value
after plus-equals: property += value.  
[Column](Unity.Android.Gradle.AssignType.Column.html)| Places value after a
column: property : value.  
[Parentheses](Unity.Android.Gradle.AssignType.Parentheses.html)| Places value
in parentheses: property(value).  
[Brackets](Unity.Android.Gradle.AssignType.Brackets.html)| Places value in
brackets: property [value].  
[EqualsBrackets](Unity.Android.Gradle.AssignType.EqualsBrackets.html)| Places
value in brackets after an equals: property = [value].  
[SetFunction](Unity.Android.Gradle.AssignType.SetFunction.html)| Places value
in a set function: property.set(value).  
  
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

