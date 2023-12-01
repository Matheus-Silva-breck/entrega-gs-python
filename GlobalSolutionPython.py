# Definindo as credenciais (substitua por valores reais)
usuario_cadastrado = "exemploemail@gmail.com"
senha_cadastrada = "senha123"

# Tela de Login
while True:
    email_input = input("Email: ").lower()
    senha_input = input("Senha: ")

    if email_input == usuario_cadastrado and senha_input == senha_cadastrada:
        print("Login bem-sucedido!\n")
        break
    else:
        print("Email ou senha incorretos. Tente novamente.")

# DADOS FÍSICOS
peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = peso / (altura ** 2)

# HISTÓRICO MÉDICO
condicoes = input("Você tem alguma condição médica preexistente, além do Diabetes? (Sim/Não) ").lower()
if condicoes == "sim":
    condicoes = input("Quais? (separe por vírgulas) ").split(', ')
else:
    condicoes = []

lista_medicamentos = input("Está tomando algum medicamento atualmente? (Sim/Não) ").lower()
if lista_medicamentos == "sim":
    lista_medicamentos = input("Quais? (separe por vírgulas) ").split(', ')
else:
    lista_medicamentos = []

lista_cirurgias = input("Já teve alguma cirurgia? (Sim/Não) ").lower()
if lista_cirurgias == "sim":
    lista_cirurgias = input("Quais? (separe por vírgulas) ").split(', ')
else:
    lista_cirurgias = []

# HISTÓRICO FAMILIAR
problemas_familiares = input("Existem problemas de saúde que ocorrem com frequência em sua família? (Sim/Não) ").lower()
if problemas_familiares == "sim":
    problemas_familiares = input("Quais? (separe por vírgulas) ").split(', ')
else:
    problemas_familiares = []

# ALIMENTAÇÃO GERAL
dieta_saudavel = int(input("Em quantos dos últimos SETE DIAS seguiu uma dieta saudável? "))
orientacoes_nutricao = int(input("Durante o último mês, QUANTOS DIAS POR SEMANA, em média, seguiu orientações alimentares dadas por um profissional de nutrição? "))

# ESTILO DE VIDA E HÁBITOS
exercicio_fisico = int(input("Em quantos dos últimos SETE DIAS praticou algum tipo de exercício físico específico? "))

fuma = input("Você fuma? (Sim/Não) ").lower()
if fuma == "sim":
    cigarros_por_dia = int(input("Quantos cigarros por dia? "))
else:
    cigarros_por_dia = 0

consumo_alcool = input("Com que frequência você consome álcool durante uma semana? (Nunca, Raramente, Moderadamente, Regularmente) ").lower()

estresse = input("Você enfrenta níveis elevados de estresse regularmente? (Sim/Não) ").lower()

# HÁBITOS DE SONO
dificuldade_adormecer = int(input("Você tem dificuldade para adormecer? (1-Sim, 2-Não) "))
acorda_frequentemente = int(input("Acorda frequentemente durante a noite? (1-Sim, 2-Não) "))
descansado_ao_acordar = int(input("Sente-se descansado ao acordar? (1-Sim, 2-Não) "))
qualidade_sono = int(input("Como você classificaria a qualidade do seu sono de 1 a 10 (sendo 1 muito ruim e 10 excelente)? "))

# QUESTÕES RELACIONADAS APENAS AO DIABETES
# ALIMENTAÇÃO ESPECÍFICA
frutas_vegetais = int(input("Em quantos dos últimos SETE DIAS comeu cinco ou mais porções de frutas e/ou vegetais? "))
gordura_rica = int(input("Em quantos dos últimos SETE DIAS comeu alimentos ricos em gordura, como carnes vermelhas ou alimentos com leite integral ou derivados? "))
doces = int(input("Em quantos dos últimos SETE DIAS comeu doces? "))

# MONITORIZAÇÃO DA GLICEMIA
glicose_avaliada = int(input("Em quantos dos últimos SETE DIAS avaliou o nível de glicose (açúcar) no sangue? "))
glicose_recomendada = int(input("Em quantos dos últimos SETE DIAS avaliou o nível de glicose (açúcar) no sangue o número de vezes recomendado pelo seu médico? "))
glicose_maior_recomendada = int(input("Em quantos dos últimos SETE DIAS o nível de glicose (açúcar) no sangue esteve maior do que o recomendado? "))

# MEDICAÇÃO
medicacao_diabetes = int(input("Em quantos dos últimos SETE DIAS tomou seus medicamentos do diabetes e/ou insulina, conforme o recomendado pelo seu médico? "))

# Mostrar resultado apenas no relatório final
print("\nRelatório Final:")
print(f"IMC: {imc:.2f}")
print("Condições Médicas:", condicoes)
print("Medicamentos:", lista_medicamentos)
print("Cirurgias:", lista_cirurgias)
print("Problemas de Saúde na Família:", problemas_familiares)
print(f"Seguiu uma dieta saudável em {dieta_saudavel} dos últimos SETE DIAS.")
print(f"Seguiu orientações alimentares em média {orientacoes_nutricao} dias por semana.")
print(f"Praticou exercício físico em {exercicio_fisico} dos últimos SETE DIAS.")
print(f"Fuma: {fuma}, Cigarros por dia: {cigarros_por_dia}")
print(f"Consumo de Álcool: {consumo_alcool}")
print(f"Enfrenta níveis elevados de estresse regularmente: {estresse}")
print("Hábitos de Sono:")
print(f"Dificuldade para adormecer: {dificuldade_adormecer == 1}")
print(f"Acorda frequentemente durante a noite: {acorda_frequentemente == 1}")
print(f"Sente-se descansado ao acordar: {descansado_ao_acordar == 1}")
print(f"Qualidade do sono (1 a 10): {qualidade_sono}")

# QUESTÕES RELACIONADAS APENAS AO DIABETES
print("Questões Relacionadas ao Diabetes:")
print(f"Comeu cinco ou mais porções de frutas e/ou vegetais em {frutas_vegetais} dos últimos SETE DIAS.")
print(f"Comeu alimentos ricos em gordura em {gordura_rica} dos últimos SETE DIAS.")
print(f"Comeu doces em {doces}")
