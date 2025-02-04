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

#  [SerializedProperty](SerializedProperty.html).numericType

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

public [SerializedPropertyNumericType](SerializedPropertyNumericType.html)
numericType;

### Description

Return the precise type for Integer and Floating point properties. (Read Only)

The [propertyType](SerializedProperty-propertyType.html) property classifies
all supported Integer types as
[SerializedPropertyType.Integer](SerializedPropertyType.Integer.html), and
both single and double precision Float types as
[SerializedPropertyType.Float](SerializedPropertyType.Float.html). This
property exposes the precise type, for example
[SerializedPropertyNumericType.UInt8](SerializedPropertyNumericType.UInt8.html)
and
[SerializedPropertyNumericType.Double](SerializedPropertyNumericType.Double.html),
and is more efficient than using the string-based [type](SerializedProperty-
type.html) property. For enum properties
([SerializedPropertyType.Enum](SerializedPropertyType.Enum.html)) it returns
the underlying type. For non-numeric types it returns
[SerializedPropertyNumericType.Unknown](SerializedPropertyNumericType.Unknown.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public class NumericTypeExample : [ScriptableObject](ScriptableObject.html)
    {
        public byte m_byte;
        public int m_int;
        public long m_long;
        public float m_float;
        public double m_double;  
      
        [[Flags](Unity.IO.LowLevel.Unsafe.AsyncReadManagerMetrics.Flags.html)]
        public enum UIntFlags : uint
        {
            None = 0,
            Flag31 = 1 << 30,
            Flag32 = 1u << 31,
        }
        public UIntFlags m_uintFlags;
        public string m_string;  
      
        [[MenuItem](MenuItem.html)("Example/[SerializedProperty](SerializedProperty.html) NumericType API")]
        static void TestMethod()
        {
            // This example demonstrates how numericType exposes more precise details of the type
            NumericTypeExample obj = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<NumericTypeExample>();
            [SerializedObject](SerializedObject.html) serializedObject = new [SerializedObject](SerializedObject.html)(obj);  
      
            var serializedProperty = serializedObject.FindProperty("m_byte");
            var sb = new StringBuilder();
            do
            {
                sb.AppendLine(String.Format("Name: {0,-11} propertyType: {1,-7} numericType: {2}",
                    serializedProperty.name, serializedProperty.propertyType, serializedProperty.numericType));
            }
            while (serializedProperty.Next(false));  
      
            //Expected output:
            //Name: m_byte      propertyType: Integer numericType: UInt8
            //Name: m_int       propertyType: Integer numericType: Int32
            //Name: m_long      propertyType: Integer numericType: Int64
            //Name: m_float     propertyType: Float   numericType: Float
            //Name: m_double    propertyType: Float   numericType: Double
            //Name: m_uintFlags propertyType: Enum    numericType: UInt32
            //Name: m_string    propertyType: String  numericType: Unknown
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

