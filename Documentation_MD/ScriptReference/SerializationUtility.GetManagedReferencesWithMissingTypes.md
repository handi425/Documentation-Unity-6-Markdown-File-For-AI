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
[SerializationUtility](SerializationUtility.html).GetManagedReferencesWithMissingTypes

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

public static ManagedReferenceMissingType[]
GetManagedReferencesWithMissingTypes([Object](Object.html) obj);

### Description

Returns the list of managed references that could not be deserialized because
of a missing type.

This method returns the list of Managed References objects that could not be
deserialized because their type is missing. This information can be used to
help resolve missing type occurrences.  
  
Additional resources:
[HasManagedReferencesWithMissingTypes](SerializationUtility.HasManagedReferencesWithMissingTypes.html),
[ManagedReferenceMissingType](ManagedReferenceMissingType.html).

    
    
    using System.Collections.Generic;
    using System.Text;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class GetManagedReferencesWithMissingTypesExample
    {
        enum ReportFormat { Detailed, ClassList }  
      
        [[MenuItem](MenuItem.html)("Example/Report [MonoBehaviour](MonoBehaviour.html) Missing [SerializeReference](SerializeReference.html) Types")]
        static public void ReportMissingTypes()
        {
            ReportMissingTypesOnActiveMonoBehaviours(ReportFormat.ClassList);
        }  
      
        [[MenuItem](MenuItem.html)("Example/Report [MonoBehaviour](MonoBehaviour.html) Missing [SerializeReference](SerializeReference.html) Types - Detailed")]
        static public void ReportMissingTypesDetailed()
        {
            ReportMissingTypesOnActiveMonoBehaviours(ReportFormat.Detailed);
        }  
      
        static private void ReportMissingTypesOnActiveMonoBehaviours(ReportFormat reportType)
        {
            var report = new StringBuilder();  
      
            // Visit all the active MonoBehaviours
            var myMonoComponents = Object.FindObjectsOfType<[MonoBehaviour](MonoBehaviour.html)>();
            foreach (var monoBehaviour in myMonoComponents)
            {
                ReportReferencesWithMissingTypesOnHost(monoBehaviour, ref report, reportType);
            }  
      
            if (report.Length == 0)
                report.Append("No missing types found");  
      
            [Debug.Log](Debug.Log.html)(report.ToString());
        }  
      
        static private void ReportReferencesWithMissingTypesOnHost(Object host, ref StringBuilder report, ReportFormat reportType)
        {
            // Report the references that have missing types on an individual [MonoBehaviour](MonoBehaviour.html), [ScriptableObject](ScriptableObject.html) or other host
            if (![SerializationUtility.HasManagedReferencesWithMissingTypes](SerializationUtility.HasManagedReferencesWithMissingTypes.html)(host))
                return;  
      
            var missingTypes = [SerializationUtility.GetManagedReferencesWithMissingTypes](SerializationUtility.GetManagedReferencesWithMissingTypes.html)(host);  
      
            report.Append(reportType == ReportFormat.Detailed ? "Missing references on " : "Missing classes on ");
            MonoBehaviourDescription(host, ref report);  
      
            if (reportType == ReportFormat.Detailed)
            {
                foreach (var missingType in missingTypes)
                {
                    report.Append("\t").AppendFormat("{0} - {1}", missingType.referenceId, MissingClassFullName(missingType));
                    if (missingType.serializedData.Length > 0)
                        report.Append("\t").AppendFormat("\n\t\t{0}", missingType.serializedData);
                    report.AppendLine();
                }
            }
            else
            {
                // Only report each unique class that is missing, rather than all objects using that class
                var missingClasses = new HashSet<string>();
                foreach (var missingType in missingTypes)
                {
                    missingClasses.Add(MissingClassFullName(missingType));
                }  
      
                foreach (var missingClass in missingClasses)
                {
                    report.Append("\t").Append(missingClass).AppendLine();
                }
            }
        }  
      
        static private void MonoBehaviourDescription(Object host, ref StringBuilder stringBuilder)
        {
            // Identify the object that has missing types
            stringBuilder.AppendFormat("[MonoBehaviour](MonoBehaviour.html) \"{0}\" (Type: {1}, Instance: {2})",
                host.name,
                host.GetType().FullName,
                host.GetInstanceID()).AppendLine();
        }  
      
        static private string MissingClassFullName([ManagedReferenceMissingType](ManagedReferenceMissingType.html) missingType)
        {
            var description = new StringBuilder();
            if (missingType.namespaceName.Length > 0)
                description.Append(missingType.namespaceName).Append(".");
            description.AppendFormat("{0}, {1}", missingType.className, missingType.assemblyName);
            return description.ToString();
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

