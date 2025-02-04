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

#  [TypeCache](TypeCache.html).GetTypesDerivedFrom

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

public static [TypeCache.TypeCollection](TypeCache.TypeCollection.html)
GetTypesDerivedFrom();

## Declaration

public static [TypeCache.TypeCollection](TypeCache.TypeCollection.html)
GetTypesDerivedFrom(Type parentType);

## Declaration

public static [TypeCache.TypeCollection](TypeCache.TypeCollection.html)
GetTypesDerivedFrom(string assemblyName);

## Declaration

public static [TypeCache.TypeCollection](TypeCache.TypeCollection.html)
GetTypesDerivedFrom(Type parentType, string assemblyName);

### Parameters

parentType | Type of a class or interface.  
---|---  
assemblyName | Optional assembly name.  
  
### Returns

**TypeCollection** Returns an unordered collection of derived types. If
assemblyName is specified, returns only types defined in this assembly.

### Description

Retrieves an unordered collection of types derived from the **T** type.

This method provides fast access to all classes loaded from a given assembly
or all Unity domain assemblies, which are derived from a specific class or
implement a specific interface. Base class or interface can be a generic. The
order of results is undefined.

    
    
    using [UnityEditor](UnityEditor.html);  
      
    public class Example
    {
        static void ScanAssetPostprocessors()
        {
            var extractedTypes = [TypeCache.GetTypesDerivedFrom](TypeCache.GetTypesDerivedFrom.html)<[AssetPostprocessor](AssetPostprocessor.html)>();
            foreach (var editors in extractedTypes)
            {
                //...
            }
        }
    }
    

Or classes which implement a specific interface.

    
    
    using [UnityEditor](UnityEditor.html);  
      
    public interface IExampleInterface {}  
      
    public class Example
    {
        static void ScanInterfaceImplementers()
        {
            var extractedTypes = [TypeCache.GetTypesDerivedFrom](TypeCache.GetTypesDerivedFrom.html)<IExampleInterface>();
            foreach (var editors in extractedTypes)
            {
                //...
            }
        }
    }
    

**Note:** The returned [TypeCollection](TypeCache.TypeCollection.html) is
read-only and thread-safe. The order of types in the collection is undefined.

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

