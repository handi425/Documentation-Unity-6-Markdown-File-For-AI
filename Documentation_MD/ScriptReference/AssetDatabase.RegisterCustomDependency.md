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

#  [AssetDatabase](AssetDatabase.html).RegisterCustomDependency

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

public static void RegisterCustomDependency(string dependency,
[Hash128](Hash128.html) hashOfValue);

### Parameters

dependency | Name of dependency. You can use any name you like, but because these names are global across all your Assets, it can be useful to use a naming convention (eg a path-based naming system) to avoid clashes with other custom dependency names.  
---|---  
hashOfValue | A Hash128 value of the dependency.  
  
### Description

Allows you to register a custom dependency that Assets can be dependent on. If
you register a custom dependency, and specify that an Asset is dependent on
it, then the Asset will get re-imported if the custom dependency changes.

If an asset has a dependency to a custom dependency and the hash value of the
custom dependency is changed, then the asset will get reimported. You can
change the hash by calling RegisterCustomDependency again, and passing the
same name, and a new value for the hash.  
  
The reimport happens when either AssetDatabase.Refresh is called or it
imported using AssetDatabase.ImportAsset().  
  
For an example for how to use custom dependencies goto
[AssetImportContext.DependsOnCustomDependency](AssetImporters.AssetImportContext.DependsOnCustomDependency.html)  
  
**Exception**  
You should not call RegisterCustomDependency from any code that is executed
during the Asset import process. If you do, this method will throw an
exception.

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

