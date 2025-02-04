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

# TypeCache

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

Provides methods for fast type extraction from assemblies loaded into the
Unity Domain.

Use `TypeCache` to access attributes and derived types information. This cache
allows arbitrary Editor code to achieve better performance, compared to using
System.Reflection, by leveraging a native cached type information.  
  
It is a common use case to extract types marked with a specific attribute, or
for classes that extend or implement a specific type, when building or
extending the Unity Editor. Iterating types in the current domain is usually a
slow operation that scales linearly based on the number of types.  
  
To speed up type extraction, the Editor builds an acceleration table, on the
native side, that contains information about type attributes and derived
classes and interfaces.

    
    
    using [UnityEditor](UnityEditor.html);
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Linq;  
      
    public class VolumeComponent {}  
      
    public class Example
    {
        static List<Type> s_VolumeComponents;
        static Example()
        {
            s_VolumeComponents = [TypeCache.GetTypesDerivedFrom](TypeCache.GetTypesDerivedFrom.html)<VolumeComponent>().ToList();
        }
    }
    

### Static Methods

[GetFieldsWithAttribute](TypeCache.GetFieldsWithAttribute.html)| Retrieves an
unordered collection of fields marked with the T attribute.  
---|---  
[GetMethodsWithAttribute](TypeCache.GetMethodsWithAttribute.html)| Retrieves
an unordered collection of methods marked with the T attribute.  
[GetTypesDerivedFrom](TypeCache.GetTypesDerivedFrom.html)| Retrieves an
unordered collection of types derived from the T type.  
[GetTypesWithAttribute](TypeCache.GetTypesWithAttribute.html)| Retrieves an
unordered collection of types marked with the T attribute.  
  
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

