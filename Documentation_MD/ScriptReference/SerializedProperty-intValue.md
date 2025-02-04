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

#  [SerializedProperty](SerializedProperty.html).intValue

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

public int intValue;

### Description

Value of an integer property.

Contains a valid value when [propertyType](SerializedProperty-
propertyType.html) is
[SerializedPropertyType.Integer](SerializedPropertyType.Integer.html) and the
underlying type is signed 32 bit or smaller (e.g. sbyte, short and int). It is
also appropriate for small unsigned types (ushort and byte). For 32 bit
unsigned fields use [uintValue](SerializedProperty-uintValue.html) instead.
And if you are accessing 64 bit integers use [longValue](SerializedProperty-
longValue.html) or [ulongValue](SerializedProperty-ulongValue.html) instead.  
  
When assigning a value to [intValue](SerializedProperty-intValue.html), the
value is clamped in the range of the property's declared type. For example, a
property that is declared as a byte is clamped between 0 and 255.  
  
Additional resources: [intValue](SerializedProperty-intValue.html),
[uintValue](SerializedProperty-uintValue.html),
[longValue](SerializedProperty-longValue.html),
[propertyType](SerializedProperty-propertyType.html),
[SerializedPropertyType.Integer](SerializedPropertyType.Integer.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class IntegerTypeExample : [ScriptableObject](ScriptableObject.html)
    {
        public sbyte m_sbyte = SByte.MinValue;
        public byte m_byte = Byte.MaxValue;
        public short m_short = Int16.MinValue;
        public ushort m_ushort = UInt16.MaxValue;
        public int m_int = Int32.MinValue;
        public uint m_uint = UInt32.MaxValue;
        public long m_long = Int64.MinValue;
        public ulong m_ulong  = UInt64.MaxValue;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) Integer Access APIs")]
        static void TestMethod()
        {
            // This example demonstrates how to access the full range of each C# integer type via [SerializedProperty](SerializedProperty.html)  
      
            IntegerTypeExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<IntegerTypeExample>();
            [SerializedObject](SerializedObject.html) sObj = new [SerializedObject](SerializedObject.html)(obj);  
      
            var sb = new StringBuilder();
            sb.AppendLine($"m_sbyte  : {sObj.FindProperty("m_sbyte").intValue}");
            sb.AppendLine($"m_byte   : {sObj.FindProperty("m_byte").uintValue}"); // or intValue
            sb.AppendLine($"m_short  : {sObj.FindProperty("m_short").intValue}");
            sb.AppendLine($"m_ushort : {sObj.FindProperty("m_ushort").uintValue}"); // or intValue
            sb.AppendLine($"m_int    : {sObj.FindProperty("m_int").intValue}");
            sb.AppendLine($"m_uint   : {sObj.FindProperty("m_uint").uintValue}");
            sb.AppendLine($"m_long   : {sObj.FindProperty("m_long").longValue}");
            sb.AppendLine($"m_ulong  : {sObj.FindProperty("m_ulong").ulongValue}");  
      
            [Debug.Log](Debug.Log.html)(sb.ToString());
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

