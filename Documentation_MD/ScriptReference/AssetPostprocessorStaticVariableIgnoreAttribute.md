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

# AssetPostprocessorStaticVariableIgnoreAttribute

class in UnityEditor

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

Allows you to decorate static variables in AssetPostprocessor and
ScriptedImporter classes that should be ignored by the static variable warning
system in the Import Activity window.  
  
This attribute is introduced to decorate static variables in PostProcessors
and ScripttedImporters to prevent warnings about the usage of static
variables. Though static variables in these classes can lead to subtle bugs
when running on different Asset Import Workers as each worker has its own Mono
Domain separate from the Main Editor, this attribute has been added to reduce
the noise which could be generated in some difficult to fix situations
involving static variables in said clasess.

Note: The static variable warnings are accessible through the "Analyze Import
Process" button in the Import Activity Window.  
  
Static variables in AssetPostprocessor or ScriptedImporter classes can lead to
unexpected behavior because their values are not shared across the different
domains in the Main Editor and Asset Import Workers. When you modify a static
variable in the Main Editor and expect the value to be reflected in the worker
on its own domain, the value will not be updated, which may result in
unexpected behavior.

    
    
    using [UnityEditor](UnityEditor.html);  
      
    public class PostProcessorWithStaticVariable : [AssetPostprocessor](AssetPostprocessor.html)
    {
       [AssetPostprocessorStaticVariableIgnore]
       public static bool enabled = false;  
      
       static void OnPostprocessAllAssets(string[] importedAssets, string[] deletedAssets, string[] movedAssets, string[] movedFromAssetPaths, bool didDomainReload)
       {
         if(enabled == false)
           return;  
      
          //do something else
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

